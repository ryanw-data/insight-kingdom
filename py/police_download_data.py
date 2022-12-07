from police_api import PoliceAPI
from datetime import datetime
import utils
api = PoliceAPI()

def get_forces():

    forces = api.get_forces()

    forces_list = []

    for force in forces:
        force_entry = {"id": force.id,
                       "name": force.name,
                       "description": force.description,
                       "url": force.url,
                       "telephone": force.telephone,
                       "_created_at":datetime.now().strftime("%d%m%Y%H%M%S%f")}

        forces_list.append(force_entry)
        keys = forces_list[0].keys()

    force_metadata_path = '../data/downloads/police-uk/metadata/'
    timestamp = datetime.now().strftime("%d%m%Y%H%M%S%f")
    force_csv_name = 'forces_{0}.csv'.format(timestamp)

    utils.create_csv_from_list(forces_list, keys, force_metadata_path, force_csv_name)

def get_neighbourhoods(start_item=0):

    forces = api.get_forces()

    num_forces = len(forces)

    force_counter = start_item + 1

    for force in forces[start_item:]:

        neighbourhood_list = []

        num_neighbourhoods = len(force.neighbourhoods)

        neighbourhood_counter = 1

        for neighbourhood in force.neighbourhoods:
            print(f"Force number {force_counter} of {num_forces}... "
                  f"Neighbourhood number {neighbourhood_counter} of {num_neighbourhoods}.")

            neighbourhood_entry = {"force_id": force.id,
                                   "id": neighbourhood.id,
                                   "name": neighbourhood.name,
                                   "description": neighbourhood.description,
                                   "url_force": neighbourhood.url_force,
                                   "population": neighbourhood.population,
                                   "locations": neighbourhood.locations,
                                   "boundary": neighbourhood.boundary,
                                   "contact_details": neighbourhood.contact_details,
                                   "_created_at": datetime.now().strftime("%d%m%Y%H%M%S%f")
                                   }

            neighbourhood_list.append(neighbourhood_entry)

            neighbourhood_counter = neighbourhood_counter + 1

        keys = neighbourhood_list[0].keys()
        csv_metadata_path = '../data/downloads/police-uk/metadata/neighbourhoods/'
        timestamp = datetime.now().strftime("%d%m%Y%H%M%S%f")
        csv_name = 'neighbourhoods_{0}_{1}.csv'.format(force.id, timestamp)

        utils.create_csv_from_list(neighbourhood_list, keys, csv_metadata_path, csv_name)

        force_counter = force_counter + 1