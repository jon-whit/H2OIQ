/*
 * station.h - A library for H2OIQ watering stations.
 * Created by Jonathan Whitaker and Daniel Houston
 * Date: April 27, 2015
 */

#ifndef STATION_H
#define STATION_H

#include <XBee.h>

class station {

private:
  // private member variables
  xbee _xbee;
  int _station_id;
  int _battery_life;

  // private member functions
  void actuate_servo();

public:

  // public constructor and destructor
  station(XBee);
  ~station();

  // public member functions
  bool register_station();
  void start_watering();
  void stop_watering();
  int read_moitsure();


};

 #endif
