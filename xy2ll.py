CMS_INCH = 2.54; 		/* cms/inch */
METERS_FOOT = 0.3048; 		/* meters/foot */
METERS_NMILE = 1852.0; 		/* meters/nautical mile */
METERS_FATHOM = 1.8288;  	/* meters/fathom (straight conversion) */
UMETERS_UFATHOM = 1.8750; 	/* unc mtrs/unc fthm - accounts for */
				/* snd vel of 1500m/sec to 800fm/sec */
PI = 3.1415927;
TWO_PI = 6.2831854;  
RTOD =57.29577951308232; 
DTOR =(1.0/RTOD); 
RADIANS = 57.2957795; 		/* degrees/radian */
SECS_HOUR = 3600; 
/* coordinate translation options */
XY_TO_LL= 1;
LL_TO_XY= 2;
LL_TO_LL= 3;

/* coordinate system types  */
GPS_COORDS_WGS84 = 1;
GPS_COORDS_C1866 = 2;
LORANC_COORDS = 3;
SURVEY_COORDS = 4;
TRANSIT_COORDS = 5;

RADIUS = 6378137.0;
FLATTENING = 0.00335281068; /* GRS80 or WGS84 */
K_NOT = 0.9996;     /* UTM scale factor */
DEGREES_TO_RADIANS = 0.01745329252;
FALSE_EASTING = 500000.0;
FALSE_NORTHING = 10000000.0;

function DEG_TO_RADIANS(x)
{ 
    return (x/RADIANS); 
}

function RAD_TO_DEGREES(x)
{  
    return (x*RADIANS); 	/* radians (a) to degrees */
}


function METERS_DEGLON(x)
{  
   with (Math)
   {
      var d2r=DEG_TO_RADIANS(x);
      return((111415.13 * cos(d2r))- (94.55 * cos(3.0*d2r)) + (0.12 * cos(5.0*d2r)));
   }
}
function METERS_DEGLAT(x)
{
   with (Math)
   {
      var d2r=DEG_TO_RADIANS(x);
      return(111132.09 - (566.05 * cos(2.0*d2r))+ (1.20 * cos(4.0*d2r)) - (0.002 * cos(6.0*d2r)));
   }
}

/*----------------------------------------------------------
#   The following functions are modified from the origin
#   C functions created by Louis Whitcomb 19 Jun 2001
 ---------------------------------------------------------*/
/*----------------------------------------------------------
#   translate_coordinates
#   routine to translate between geographic and cartesian coordinates
#   user must supply following data on the cartesian coordinate system:
#   location of the origin in lat/lon degrees;
#   rotational skew from true north in degrees;
#   N.B. sense of rotation i/p here is exactly as o/p by ORIGIN
#   x/y offset in meters - only if an offset was used during the
#   running of prog ORIGIN;
*/

function translate_coordinates(trans_option,porg)
{
   with(Math)
   {   
      var xx,yy,r,ct,st,angle;
      angle = DEG_TO_RADIANS(porg.rotation_angle_degs);

      if( trans_option == XY_TO_LL)
      {
         /* X,Y to Lat/Lon Coordinate Translation  */
         pxpos_mtrs = porg.x;  
         pypos_mtrs = porg.y;
	 xx = pxpos_mtrs - porg.xoffset_mtrs;
	 yy = pypos_mtrs - porg.yoffset_mtrs;
	 r = sqrt(xx*xx + yy*yy);

	 if(r)
	 {
            ct = xx/r;
	    st = yy/r;
	    xx = r * ( (ct * cos(angle))+ (st * sin(angle)) );
	    yy = r * ( (st * cos(angle))- (ct * sin(angle)) );
	 }

	 var plon = porg.olon + xx/METERS_DEGLON(olat);
	 var plat = porg.olat + yy/METERS_DEGLAT(olat);

         var sll={};
         sll={slat:plat, slon:plon};
         return(sll);
      }

