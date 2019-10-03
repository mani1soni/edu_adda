#include <iostream>
#include <string>
using namespace std;


class ADT
{
public:
    string name;
    string location;
    double price = 0.0;
    virtual int getCapacity();
    virtual int getPowerConsumption();
    virtual int getChannels();
    virtual string getFavSong();
    virtual void special();
    virtual double getFrequency();
    virtual int getSpeakers();
    virtual void setCapacity(int);
    virtual void setPowerConsumption(int);
    virtual void setChannels(int);
    virtual void setFavSong(string);
    virtual void setFrequency(double);
    virtual void setSpeakers(int);
    string getName();
    string getLocation();
    double getPrice();
    void setName(string);
    void setLocation(string);
    void setPrice(double);
};

class HouseholdAppliance: public ADT
{
protected:
    double power = 0.0;
public:
    void special() override;
    void setPower(double);
    double getPower();
};
class Media: public ADT
{
protected:
    double quality = 0.0;
public:
    void special() override;
    void setQuality(double);
    double getQuality();
};
class WashingMachine: public HouseholdAppliance
{
public:
    int capacity = 0;
    void special();
    void setCapacity(int);
    int getCapacity();
};
class VacuumCleaner: public HouseholdAppliance
{
public:
    int powerConsumption = 0;
    void special();
    void setPowerConsumption(int);
    int getPowerConsumption();
};
class TV: public HouseholdAppliance
{
public:
    int channels = 0;
    void special();
    void setChannels(int);
    int getChannels();
};
class Audio: public Media
{
public:
    string favSong;
    void special();
    void setFavSong(string);
    string getFavSong();
};
class Radio: public Media
{
public:
    double frequency = 0.0;
    void special();
    void setFrequency(double);
    double getFrequency();
};
class MusicCenter: public Media
{
public:
    int speakers = 0;
    void special();
    void setSpeakers(int);
    int getSpeakers();
};
