/*
 * station.h - A library for H2OIQ watering stations.
 * Created by Jonathan Whitaker and Daniel Houston
 * Date: April 27, 2015
 */

#ifndef STATION_H
#define STATION_H

#include "Arduino.h"
#include "XBee.h"

class station {

private:
  // private member variables
  xbee _xbee;
  int _station_id;
  int _battery_life;

  // private member functions
  void actuate_servo(bool);

public:

  // public constructor and destructor
  station(XBee);
  ~station();

  // public member functions
  bool register_station();
  void start_watering();
  void stop_watering();
  int read_moitsure();

  // relational operators
  inline bool operator< (const station& lhs, const station& rhs){ return lhs._station_id < rhs._station_id;}
  inline bool operator> (const station& lhs, const station& rhs){return rhs < lhs;}
  inline bool operator<=(const station& lhs, const station& rhs){return !(lhs > rhs);}
  inline bool operator>=(const station& lhs, const station& rhs){return !(lhs < rhs);}
  inline bool operator==(const X& lhs, const X& rhs){ return lhs._station_id == rhs._station_id; }
  inline bool operator!=(const X& lhs, const X& rhs){return !(lhs == rhs);}

};

 #endif
