#include "lab7.h"


////ADT helper class
int ADT::getCapacity() {}
int ADT::getChannels() {}
int ADT::getPowerConsumption() {}
int ADT::getSpeakers() {}
double ADT::getFrequency() {}
string ADT::getFavSong() {}
void ADT::setCapacity(int) {}
void ADT::setPowerConsumption(int) {}
void ADT::setChannels(int) {}
void ADT::setFavSong(string) {}
void ADT::setFrequency(double) {}
void ADT::setSpeakers(int) {}
void ADT::special() {};
string ADT::getName()
{
    return name;
}
string ADT::getLocation()
{
    return location;
}
double ADT::getPrice()
{
    return price;
}
void ADT::setName(string iName)
{
    this->name = iName;
}
void ADT::setLocation(string iLocation)
{
this->location = iLocation;
}
void ADT::setPrice(double iPrice)
{
    this->price = iPrice;
}

void HouseholdAppliance::special()
{
    cout << "I am an item in your house" << endl;
}

void HouseholdAppliance::setPower(double iPower)
{
    this->power = iPower;
}
double HouseholdAppliance::getPower()
{
    return power;
}

void Media::setQuality(double iQuality)
{
    this->quality = iQuality;
}
double Media::getQuality()
{
    return quality;
}
void Media::special()
{
    cout << "I am a music item in your house" << endl;
}

//WashingMachine class
void WashingMachine::special()
{
    cout << "I am " << name << " and I wash your stuff!" << endl;
}
void WashingMachine::setCapacity(int iCapacity)
{
    this->capacity = iCapacity;
}
int WashingMachine::getCapacity()
{
    return capacity;
}
//VacuumCleaner class
void VacuumCleaner::special()
{
    cout << "I am " << name << " and I tidy your house!" << endl;
}
void VacuumCleaner::setPowerConsumption(int iPC)
{
    this->powerConsumption = iPC;
}
int VacuumCleaner::getPowerConsumption()
{
    return powerConsumption;
}
//TV class
void TV::special()
{
    cout << "I am " << name << " and I help you to relax!" << endl;
}
void TV::setChannels(int iChannels)
{
    this->channels = iChannels;
}
int TV::getChannels()
{
    return channels;
}
//Audio class
void Audio::special()
{
    cout << "I am " << name << " and I know your favourite song!" << endl;
}
void Audio::setFavSong(string iSong)
{
    this->favSong = iSong;
}
string Audio::getFavSong()
{
    return favSong;
}
//Radio class
void Radio::special()
{
    cout << "I am " << name << " and I am as old as you!" << endl;
}
void Radio::setFrequency(double iFrequency)
{
    this->frequency = iFrequency;
}
double Radio::getFrequency()
{
    return frequency;
}
//MusicCenter class
void MusicCenter::special()
{
    cout << "I am " << name << " and I am loud!" << endl;
}
void MusicCenter::setSpeakers(int iSpeakers)
{
    this->speakers = iSpeakers;
}
int MusicCenter::getSpeakers()
{
    return speakers;
}
