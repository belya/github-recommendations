## Pick up the data

### Prerequisites:

- Conda environment with installed packages from the project environment.yml

- Redis server installed and running


### Run tasks:
1. `$ python collect_data.py`

2. `$ huey_consumer.py -w <number_of_workers> -n collect_data.huey`
