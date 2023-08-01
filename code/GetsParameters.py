def  getsParameters_best(video):
    
    R_lower=35;    
    medP=5; 
    R_scale=0.1;
    #cameraJitter ++
    if (video == 'badminton'):
        medP=11;    R_lower=35;    R_scale=2;
    
    if (video == 'boulevard'):
        medP=3;     R_lower=70;    R_scale=2; 
    
    if (video == 'sidewalk'):
        medP=9;     R_lower=30;    R_scale=2; 
    
    if (video == 'traffic'):
        medP=9;    R_lower=55 ;   R_scale=2; 
    
    
    #badWeather ++
    if (video == 'blizzard'):
       medP=1;     R_lower=20;   R_scale=2;
    
    if (video == 'skating'):
        medP=7;     R_lower=50;    R_scale=1;
    
    if (video == 'snowFall'): 
       medP=1;     R_lower=35 ;   R_scale=2;
    
    if (video == 'wetSnow'):
        medP=1;     R_lower=50;    R_scale=2;
    
  
    #baseline oo
    if (video == 'highway'):
        medP=9;    R_lower=50;    R_scale=0.1;
    
    if (video == 'office'):
       medP=1;    R_lower=65 ;   R_scale=0.1;
    
    if (video == 'pedestrians'):
        medP=9;   R_lower=50 ;   R_scale=1;
    
    if (video == 'PETS2006'):
        medP=3;    R_lower=50;   R_scale=0.1;
    
  
    #dynamicBackground ++
    if (video == 'boats'):
        medP=9;    R_lower=25;   R_scale=1; 
    
    if (video == 'canoe'):
        medP=9;   R_lower=65;   R_scale=0.1; 
    
    if (video == 'fall'):
       medP=15;   R_lower=45 ;  R_scale=2;
    
    if (video == 'fountain01'):
       medP=15;   R_lower=20;   R_scale=2; 
    
    if (video == 'fountain02'):
       medP=11 ;  R_lower=40;   R_scale=1; 
    
    if (video == 'overpass'):
       medP=13;   R_lower=45;   R_scale=1;
    
  
  
    #intermittentObjectMotion ++
    if (video == 'abandonedBox'):
        medP=5;    R_lower=65 ;  R_scale=0.1;
    
    if (video == 'parking'):
       medP=1;    R_lower=15;    R_scale=2;
      
    if (video == 'sofa'):
        medP=9;    R_lower=20;   R_scale=0.1;
    
    if (video == 'streetLight'):
       medP=1;    R_lower=70;   R_scale=0.1;
    
    if (video == 'tramstop'):
        medP=1;    R_lower=40;   R_scale=2;
    
    if (video == 'winterDriveway'): 
        medP=5;    R_lower=55;   R_scale=2;
    
  
    #lowFramerate ++
    if (video == 'port_0_17fps'):
       medP=9;     R_lower=70 ;   R_scale=2;
    
    if (video == 'tramCrossroad_1fps'):
       medP=3;     R_lower=70;    R_scale=0.1;
    
    if (video == 'tunnelExit_0_35fps'):
        medP=9;     R_lower=40;    R_scale=0.1;
    
    if (video == 'turnpike_0_5fps'):
       medP=5;     R_lower=55;    R_scale=0.1;
    
    
 
    #nightVideos ++
    if (video == 'bridgeEntry'):
        medP=1;     R_lower=45;   R_scale=2;
    
    if (video == 'busyBoulvard'):
        medP=1;     R_lower=30;   R_scale=2;
    
    if (video == 'fluidHighway'):
       medP=1;     R_lower=65;   R_scale=2;
    
    if (video == 'streetCornerAtNight'):
       medP=1;     R_lower=70;   R_scale=2; 
    
    if (video == 'tramStation'):
       medP=5;     R_lower=30 ;  R_scale=2;
    
    if (video == 'winterStreet'):
      medP=1;     R_lower=55 ;  R_scale=2;
    
  
    #PTZ ++
    if (video == 'continuousPan'):
        medP=15;    R_lower=70;   R_scale=2;  
    
    if (video == 'intermittentPan'):
        medP=13;    R_lower=70;   R_scale=2;  
    
    if (video == 'twoPositionPTZCam'):
        medP=7;   R_lower=70;   R_scale=2;  
    
    if (video == 'zoomInZoomOut'):
         medP=11;    R_lower=70;   R_scale=2;  
    
  
    #shadow ++
    if (video == 'backdoor'):
        medP=9;     R_lower=30 ;   R_scale=2;
        
    if (video == 'bungalows'):
        medP=9;      R_lower=30;    R_scale=0.1;
    
    if (video == 'busStation'):
        medP=5;    R_lower=65;    R_scale=0.1; 
     
    if (video == 'copyMachine'):
        medP=5;     R_lower=60;    R_scale=0.1;   
    
    if (video == 'cubicle'):
        medP=1;     R_lower=60;    R_scale=2;
    
    if (video == 'peopleInShade'):
       medP=3;     R_lower=45;    R_scale=1;
    
  
  
    #thermal ++
    if (video == 'corridor'):
         medP=13;    R_lower=35;  R_scale=0.1;
    
    if (video == 'diningRoom'):
        medP=3;    R_lower=25;  R_scale=1;
    
    if (video == 'lakeSide'):      
       medP=1;     R_lower=20;  R_scale=1;
    
    if (video == 'library'):
       medP=15;     R_lower=45;  R_scale=0.1;
    
    if (video == 'park'):
       medP=1;     R_lower=50;  R_scale=0.1;
    
  
    #turbulence ++
    if (video == 'turbulence0'):
         medP=15;    R_lower=35;    R_scale=2; 
    
    if (video == 'turbulence1'):
        medP=13;    R_lower=55;   R_scale=2;
    
    if (video == 'turbulence2'):
       medP=9;     R_lower=40;    R_scale=2;
    
    if (video == 'turbulence3'):
         medP=7;    R_lower=40;    R_scale=2;
    
    
  
    return R_lower, medP, R_scale


