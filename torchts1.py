import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import torch.nn as nn

import os
import torch
import sklearn
import scipy

from datetime import datetime
from tqdm import tqdm
from scipy import stats
from platform import python_version
import utils_bsc
if torch.cuda.is_available():
  device = torch.device('cuda:0')
  print('Device: GPU =', torch.cuda.get_device_name(0))
else:
  device = torch.device('cpu')
  print('Device: CPU')

saved_results = 'training_results'
# Check whether the directory where the results files must be saved exists or not
if not os.path.exists(saved_results):
  # Create a new directory because it does not exist
  os.makedirs(saved_results)
print('versions of packages:')
print(f'Python: {python_version()}')
print(f'Pandas: {pd.__version__}')
print(f'Numpy: {np.__version__}')
print(f'PyTorch: {torch.__version__}')
print(f'Sklearn: {sklearn.__version__}')
print(f'seaborn: {sns.__version__}')
print(f'scipy: {scipy.__version__}')
# This cell is necessary to use this notebook in google colab
# If you are running this notebook in colab, please change colab to True

colab = False

if colab is True:
    cwd = os.getcwd()

    if cwd != "/content/Bsc_Thesis":
        #!git clone https://github.com/SergioTallo/Bsc_Thesis.git
        #% cd Bsc_Thesis

     print(cwd)
dataset = pd.read_csv('data_factory.csv')
# Replace all mising values with NaN
dataset = dataset.replace(' ', np.nan)
# Search for all the rows with NaN values
nan_values = dataset[dataset.isna().any(axis=1)]
# Print the shape to know how many are there
print(f'Number of rows with NaN values before cleaning: {nan_values.shape[0]}') 

# Fill all NaN values with the previous row value
dataset_clean = dataset.fillna(method='ffill')

# Check that there isn't any NaN values
nan_values = dataset_clean[dataset_clean.isna().any(axis=1)]
# Print the shape to know how many are there
print(f'Number of rows with NaN values after cleaning: {nan_values.shape[0]}') 

#Total number of samples
print(f'Total number of samples: {dataset_clean.shape[0]}')
print(f'Number of features: {dataset_clean.shape[1]}')
print_data = False
print_graphs = False
if print_data is True:
  for column in dataset_clean.columns:
    if column == 'time':
      print(column)
      print('Min value: ', dataset_clean[column].min())
      print('Max value: ', dataset_clean[column].max())
      print('')
    else:
      print(column)
      print('Min value: ', dataset_clean[column].min())
      print('Max value: ', dataset_clean[column].max())
      print('Mean value: ', dataset_clean[column].mean())
      print('Median value: ', dataset_clean[column].median())
      print('Standard deviation: ', dataset_clean[column].std())
      print('')

if print_graphs is True:

  for i, column in enumerate(dataset_clean.columns):
    if i > 0:
      # Feature in a weekly interval
      utils_bsc.week_plot(dataset_clean, i, column)
      # Feature in a daily interval (only the values of weekdays between 4:00 and 19:30)
      utils_bsc.daily_plot(dataset_clean, i, column)
# We print some graphs showing the density distribution of every feature
if print_graphs is True:
  for column in tqdm(dataset_clean.columns):
    if column != 'time':
      sns.displot(dataset_clean, x=column, kind="kde")

# We create two extra data sets, one with the weekdays between 4:00 and 18:30 and one with the rest.
dataset_clean_time = pd.to_datetime(dataset_clean['time'])

day_mask = dataset_clean_time.dt.day_name()

time_mask = (dataset_clean_time.dt.hour >= 4) & ((dataset_clean_time.dt.hour < 19) | ((dataset_clean_time.dt.hour == 19) & (dataset_clean_time.dt.minute <= 30))) & ((day_mask == ('Monday')) | (day_mask == ('Tuesday')) | (day_mask == ('Wednesday')) | (day_mask == ('Thursday')) | (day_mask == ('Friday')))

dataset_weekdays = dataset_clean[time_mask]

for i in range(len(time_mask)):
  if time_mask[i] == False:
    time_mask[i] = True
  elif time_mask[i] == True:
    time_mask[i] = False

dataset_weekend = dataset_clean[time_mask]
print(f'Weekdays dataset size: {len(dataset_weekdays)}')
print(f'Weekend dataset size: {len(dataset_weekend)}')
if print_graphs is True:
  for column in tqdm(dataset_weekdays.columns):
    if column != 'time':
      sns.displot(dataset_weekdays, x=column, kind="kde")

if print_graphs is True:
  for column in tqdm(dataset_weekend.columns):
    if column != 'time':
      sns.displot(dataset_weekend, x=column, kind="kde")
# Perform the data normalisation in the whole dataset. We can print the distribution of the data if we want.
dataset_norm = utils_bsc.normalize_mean_std_dataset(dataset_clean)

print_graphs = False

if print_graphs is True:
  for column in tqdm(dataset_norm.columns):
    if column != 'time':
      sns.displot(dataset_norm, x=column, kind="kde")
# Perform the data normalisation in the weekdays dataset. We can print the distribution of the data if we want.
dataset_weekdays_norm = utils_bsc.normalize_mean_std_dataset(dataset_weekdays)

print_graphs = False

if print_graphs is True:
  for column in tqdm(dataset_weekdays_norm.columns):
    if column != 'time':
      sns.displot(dataset_weekdays_norm, x=column, kind="kde")
# Perform the data normalisation in the weekdays dataset. We can print the distribution of the data if we want.
dataset_weekend_norm = utils_bsc.normalize_mean_std_dataset(dataset_weekend)

print_graphs = False

if print_graphs is True:
  for column in tqdm(dataset_weekend_norm.columns):
    if column != 'time':
      sns.displot(dataset_weekend_norm, x=column, kind="kde")


dataset_norm.head()
dataset_weekdays_norm.head()
dataset_weekend_norm.head()
correlations = []
matrix = []

for i in dataset_norm.columns[1:]:
  feature = []
  for j in dataset_norm.columns[1:]:
    print(f'Correlation between {i} and {j}')
    correlation = stats.pearsonr(dataset_norm[i], dataset_norm[j])[0]
    if i != j:
      correlations.append(abs(correlation))
      feature.append(abs(correlation))
      print(correlation)
  print(f'Mean of {i} correlations: {np.mean(feature)}')
  print('')
  matrix.append(feature)

print(f'Mean of all correlations: {np.mean(correlations)}')
# Features correlations heat map

corr = dataset_norm.corr()
ax = sns.heatmap(corr, cmap="Blues")
plt.show()
# Covariance matrix, eigenvalues and explained variance

covmatrix = dataset_norm.cov()
eigenvalues, eigenvectors = np.linalg.eig(covmatrix)

acc = 0

acc_variance = []

for i, eigen in enumerate(eigenvalues):
  acc += eigen/np.sum(eigenvalues)
  acc_variance.append(acc)
  print(f'Explained_variance {i +1} principal component: {eigen/np.sum(eigenvalues)} (accumulated {round(acc, 4)})')
fig = plt.figure(figsize=(15,8))

a = acc_variance

b = [i +1 for i in range(len(acc_variance))]
plt.title('Explained variance over number of principal components')
plt.xlabel('n principal components')
plt.xticks(b)
plt.ylabel('explained variance')
plt.bar(b, a)
plt.show()
loader_train, loader_test = utils_bsc.create_dataloaders(dataset=dataset_norm, device=device)
criterion = nn.MSELoss()

losses_train = []

for i in loader_train:
  output = i[0]
  target = i[1]
  loss = criterion(output, target)
  losses_train.append(loss.item())

losses_test = []

for i in loader_test:
  output = i[0]
  target = i[1]
  loss = criterion(output, target)
  losses_test.append(loss.item())

# save to npy file to keep track of the results and to print graphs
np.save(saved_results + '/baseline_train.npy', losses_train)
np.save(saved_results + '/baseline_test.npy', losses_test)
print('...............crossed this 1..........')
if colab is True:
    files.download(saved_results + '/baseline_train.npy')
    files.download(saved_results + '/baseline_test.npy')
print("Training set")
print("Mean Loss of baselinemodel: ", np.mean(losses_train))
print("Standard deviation Loss of baselinemodel: ", np.std(losses_train))
print('\n')
print("Test set")
print("Mean Loss of baselinemodel: ", np.mean(losses_test))
print("Standard deviation Loss of baselinemodel: ", np.std(losses_test))
start_train_FFN = True

# Create model FFN instance
model_FFN = utils_bsc.ANN_relu(18, 18).to(device)

print(f'Model: {type(model_FFN).__name__}')
print(f'{utils_bsc.count_parameters(model_FFN)} trainable parameters.')
print('...............crossed this 2..........')

# Define Loss
criterion = nn.MSELoss()

# Define Optimizer
learning_rate=0.01
optimizer_whole = torch.optim.SGD(model_FFN.parameters(), lr=learning_rate)

if start_train_FFN is True:
    n_epochs = 10

    params_not_trained_whole = model_FFN.parameters()

    start_time = datetime.now()

    best_results , train_losses_FFN, test_losses_FFN = utils_bsc.train_FFN(model_FFN, criterion, optimizer_whole, loader_train, loader_test, n_epochs)
    print('....printing test_losses_FFN')
    print(test_losses_FFN)

    model_FFN = best_results[0]
    best_train_loss = best_results[1]
    best_test_loss = best_results[2]
    best_epoch_number = best_results[3]

    end_time = datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds()

    print(f'Best test loss at epoch {best_epoch_number}')
    print(f'Train Loss: {best_train_loss}')
    print(f'Test Loss: {best_test_loss}')
    print(f'\nTraining time for {n_epochs} epochs: {execution_time} seconds')
    print('....................here................')

    # save to npy file
    np.save(saved_results + '/FFN_train.npy', train_losses_FFN)
    np.save(saved_results + '/FFN_test.npy', test_losses_FFN)
    torch.save(model_FFN, saved_results + '/model_FFN.pt')
    print(saved_results + '/FFN_train.npy','...saved')
    print('...............crossed this 3..........')
    if colab is True:

        from google.colab import files

        files.download(saved_results + '/FFN_train.npy')
        files.download(saved_results + '/FFN_test.npy')
        files.download(saved_results + '/model_FFN.pt')
if start_train_FFN is True:
    baseline_loss = [np.mean(losses_train) for i in range(len(train_losses_FFN))]
    utils_bsc.print_results_training(train_loss=train_losses_FFN, test_loss=test_losses_FFN, test_loss_baseline=baseline_loss, baseline_label='Baseline', title="Full Forward Neural Network train results")
training_results_transformers ={}
models = {'vanilla': [6, 1, 6, 2048, 'SGD', 0.01, None, True, 30, 16]}
print('...............crossed this 4..........')
training_results_transformers = utils_bsc.define_train_transformers(models, device, dataset_norm, training_results_transformers, saved_results, colab)
print('...............crossed this 6..........')
if models['vanilla'][7] is True:
    print(test_losses_FFN)
    baseline_loss = [np.mean(i) for i in test_losses_FFN]
    utils_bsc.print_results_training(train_loss=training_results_transformers['vanilla'][4], test_loss=training_results_transformers['vanilla'][5], test_loss_baseline=baseline_loss, baseline_label='FFN Test Loss', title="Training results " + 'vanilla' + " Transformer (" + str(models['vanilla'][0]) + " encoder layers, " + str(models['vanilla'][1]) + " decoder layer, " + str(models['vanilla'][2]) + " heads. " + models['vanilla'][4])

models['vanilla'][7] = False
models['ADAM'] = [6, 1, 6, 2048, 'ADAM', 0.001, None, True, 30, 16]
training_results_transformers = utils_bsc.define_train_transformers(models, device, dataset_norm, training_results_transformers, saved_results, colab)
if models['ADAM'][7] is True:

    baseline_loss = [np.mean(i) for i in training_results_transformers['vanilla'][5]]
    utils_bsc.print_results_training(train_loss=training_results_transformers['ADAM'][4], test_loss=training_results_transformers['ADAM'][5], test_loss_baseline=baseline_loss, baseline_label='Vanilla transformer Test Loss', title="Training results " + 'ADAM' + " Transformer (" + str(models['ADAM'][0]) + " encoder layers, " + str(models['ADAM'][1]) + " decoder layer, " + str(models['ADAM'][2]) + " heads. " + models['ADAM'][4])
models['ADAM'][7] = False
models['Momentum'] = [6, 1, 6, 2048, 'SGD', 0.001, 0.9, True, 30, 16]
training_results_transformers = utils_bsc.define_train_transformers(models, device, dataset_norm, training_results_transformers, saved_results, colab)
if models['Momentum'][7] is True:

    baseline_loss = [np.mean(i) for i in training_results_transformers['vanilla'][5]]
    utils_bsc.print_results_training(train_loss=training_results_transformers['Momentum'][4], test_loss=training_results_transformers['Momentum'][5], test_loss_baseline=baseline_loss, baseline_label='Vanilla transformer Test Loss', title="Training results " + 'Momentum' + " Transformer (" + str(models['Momentum'][0]) + " encoder layers, " + str(models['Momentum'][1]) + " decoder layer, " + str(models['Momentum'][2]) + " heads. " + models['Momentum'][4])
models['Momentum'][7] = False
models['smallest'] = [1, 1, 1, 512, 'SGD', 0.001, 0.9, True, 30, 16]
training_results_transformers = utils_bsc.define_train_transformers(models, device, dataset_norm, training_results_transformers, saved_results, colab)
if models['smallest'][7] is True:

    baseline_loss = [np.mean(i) for i in training_results_transformers['vanilla'][5]]
    utils_bsc.print_results_training(train_loss=training_results_transformers['smallest'][4], test_loss=training_results_transformers['smallest'][5], test_loss_baseline=baseline_loss, baseline_label='Vanilla transformer Test Loss', title="Training results " + 'smallest' + " Transformer (" + str(models['smallest'][0]) + " encoder layers, " + str(models['smallest'][1]) + " decoder layer, " + str(models['smallest'][2]) + " heads. " + models['smallest'][4])

models['smallest'][7] = False
models['bigger'] = [10, 5, 9, 4096, 'SGD', 0.001, 0.9, True, 30, 16]
training_results_transformers = utils_bsc.define_train_transformers(models, device, dataset_norm, training_results_transformers, saved_results, colab)
if models['bigger'][7] is True:
    baseline_loss = [np.mean(i) for i in training_results_transformers['vanilla'][5]]
    utils_bsc.print_results_training(train_loss=training_results_transformers['bigger'][4], test_loss=training_results_transformers['bigger'][5], test_loss_baseline=baseline_loss, baseline_label='Vanilla transformer Test Loss', title="Training results " + 'bigger' + " Transformer (" + str(models['bigger'][0]) + " encoder layers, " + str(models['bigger'][1]) + " decoder layer, " + str(models['bigger'][2]) + " heads. " + models['bigger'][4])
models['bigger'][7] = False
models['seq_15'] = [6, 1, 6, 2048, 'SGD', 0.001, 0.9, True, 15, 16]
models['seq_60'] = [6, 1, 6, 2048, 'SGD', 0.001, 0.9, True, 60, 16]
models['seq_2'] = [6, 1, 6, 2048, 'SGD', 0.001, 0.9, True, 2, 16]
models['seq_20'] = [6, 1, 6, 2048, 'SGD', 0.001, 0.9, True, 20, 16]
models['seq_10'] = [6, 1, 6, 2048, 'SGD', 0.001, 0.9, True, 10, 16]
models['seq_120'] = [6, 1, 6, 2048, 'SGD', 0.001, 0.9, True, 120, 16]
print(models)
training_results_transformers = utils_bsc.define_train_transformers(models, device, dataset_norm, training_results_transformers, saved_results, colab)








