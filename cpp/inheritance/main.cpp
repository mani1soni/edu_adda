#include <iostream>
#include "inheritanceClasses.cpp"
using namespace std;


int main()
{
    WashingMachine washingMachine;
    VacuumCleaner vacuumCleaner;
    TV tv;
    Audio audio;
    Radio radio;
    MusicCenter musicCenter;

    ADT * items[6] = {&washingMachine, &vacuumCleaner,
                                   &tv, &audio, &radio, &musicCenter};
    string names[6] = {"Washing machine", "Vacuum cleaner",
                       "TV", "Audio system", "Radio", "Music center"};
    string locations[6] = {"Bathroom", "Attic", "Living room",
                           "Bedroom", "Child room", "Hall"};
    double prices[6] = {200.00, 179.99, 329.99, 250.00, 199.99, 450.00};

    for (int i=0; i<6; i++)
    {
        items[i]->setName(names[i]);
        items[i]->setLocation(locations[i]);
        items[i]->setPrice(prices[i]);
        cout << "Item #" << i+1 << endl;
        cout << "Name: " << items[i]->getName() << endl;
        cout << "Location: " << items[i]->getLocation() << endl;
        cout << "Price: $" << items[i]->getPrice() << endl;
        switch (i)
        {
            case 0:
                items[i]->setCapacity(10);
                cout << "Capacity: " << items[i]->getCapacity() << endl;
                break;
            case 1:
                items[i]->setPowerConsumption(70);
                cout << "Power consumption: " << items[i]->getPowerConsumption() << endl;
                break;
            case 2:
                items[i]->setChannels(60);
                cout << "Num Channels: " << items[i]->getChannels() << endl;
                break;
            case 3:
                items[i]->setFavSong("What Is Love");
                cout << "Favourite song: " << items[i]->getFavSong() << endl;
                break;
            case 4:
                items[i]->setFrequency(91.5);
                cout << "Frequency: " << items[i]->getFrequency() << endl;
                break;
            case 5:
                items[i]->setSpeakers(4);
                cout << "Num speakers: " << items[i]->getSpeakers() << endl;
                break;
            default:
                cout << "None" << endl;
        }
        items[i]->special();
        cout << "-------------" << endl;
    }
    return 0;
}
