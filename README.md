# data-warehouse-migration-superset

[![Contributors][contributors-shield]][contributors-url][![Forks][forks-shield]][forks-url][![Stargazers][stars-shield]][stars-url][![Issues][issues-shield]][issues-url][![MIT License][license-shield]][license-url][![LinkedIn][linkedin-shield]][linkedin-url]

A project for migrating a data-warehouse tech stack built with:

- PostgreSQL
- Airflow
- dbt
- Redash

The changes performed are swapping **PostgreSQL** for **MySQL** and **Redash** for [**Apache Superset**][superset-site]

## About the data

The data is initially a video feed of drones tracking different vehicles on the road. Then this was turned into a trajectory describing format. In our data the vehicles are described with 4 columns, and the trajectories are described with 6 repeating columns that change with approximately 4 second time interval.

For each .csv file the following apply:

- each row represents the data of a single vehicle
- the first 10 columns in the 1st row include the columns’ names
(**track_id**; **type**; **traveled_d**; **avg_speed**; **lat**; **lon**; **speed**; **lon_acc**; **lat_acc**; **time**)
- the first 4 columns include information about the trajectory like the unique trackID, the type of vehicle, the distance traveled in meters and the average speed of the vehicle in km/h
- the last 6 columns are then repeated every 6 columns based on the time frequency. For example, column_5 contains the latitude of the vehicle at time column_10, and column­­­_11 contains the latitude of the vehicle at time column_16.
- Speed is in km/h, Longitudinal and Lateral Acceleration in m/sec2 and time in seconds.

## Prerequisites

Make sure you have docker installed on local machine.

- Docker: [Install guide][docker-install-guide]
- Docker-Compose: [Install guide][docker-compose-install-guide]

## Installation

1. Clone the repo

   ```sh
   git clone https://github.com/Hen0k/data-warehouse-migration-superset.git
   ```

2. Run

   ```sh
    docker-compose build
    docker-compose up
   ```

3. Open Airflow web browser

   <!-- ```JS -->
   Navigate to [http://localhost:8081/][local-airflow] on the browser
   activate and trigger all the dags
   <!-- ``` -->

4. Access dbt

   <!-- ```JS -->
   Navigate to [http://localhost:8080/][local-dbt] on the browser
   <!-- ``` -->

## Roadmap

- [ ] dummy task

## Acknowledgement

- Data source: pNEUMA – [open-traffic.epfl.ch](https://www.google.com/url?q=http://open-traffic.epfl.ch&sa=D&ust=1598884463327000&usg=AFQjCNF55kUX-00yiJbzlPzZhbgY2R4cfg)

- Airflow-with-docker-setup: [Medium blog](https://towardsdatascience.com/setting-up-apache-airflow-with-docker-compose-in-5-minutes-56a1110f4122) by [Marvin Lanhenke](https://medium.com/@marvinlanhenke)

- Airflow-DockerOperator-with-dockercompose: [Medium blog](https://towardsdatascience.com/using-apache-airflow-dockeroperator-with-docker-compose-57d0217c8219) by [Flávio Clésio](https://flavioclesio.medium.com/)

- [Multiple-users-postgres_docker-image](https://hub.docker.com/r/lmmdock/postgres-multi)

- [proper-mounting-volumes-in-DockerOperators](https://stackoverflow.com/questions/64947706/mounting-directories-using-docker-operator-on-airflow-is-not-working)

- [Redash easy installation instruction][redash-install-blog]
- [Redash basics][redash-basics]
- [Hosting dbt docs][hosting-dbt-docs]
  
<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](/LICENSE) for more information.

## Contributors

![Contributors list](https://contrib.rocks/image?repo=Hen0k/data-warehouse-migration-superset)
[Henok Tilaye][my-profile]

Made with [contrib.rocks](https://contrib.rocks).

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Hen0k/data-warehouse-migration-superset.svg?style=for-the-badge
[my-profile]: https://github.com/Hen0k
[contributors-url]: https://github.com/Hen0k/data-warehouse-migration-superset/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Hen0k/data-warehouse-migration-superset.svg?style=for-the-badge
[forks-url]: https://github.com/Hen0k/data-warehouse-migration-superset/network/members
[stars-shield]: https://img.shields.io/github/stars/Hen0k/data-warehouse-migration-superset.svg?style=for-the-badge
[stars-url]: https://github.com/Hen0k/data-warehouse-migration-superset/stargazers
[issues-shield]: https://img.shields.io/github/issues/Hen0k/data-warehouse-migration-superset.svg?style=for-the-badge
[issues-url]: https://github.com/Hen0k/data-warehouse-migration-superset/issues
[license-shield]: https://img.shields.io/github/license/Hen0k/data-warehouse-migration-superset.svg?style=for-the-badge
[license-url]: https://github.com/Hen0k/data-warehouse-migration-superset/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/henok-tilaye-b18840151/
[redash-install-blog]: https://www.techrepublic.com/article/how-to-deploy-redash-data-visualization-dashboard-help-docker/
[redash-basics]: https://hevodata.com/learn/redash/
[hosting-dbt-docs]: https://amchoi.medium.com/hosting-dbt-documentation-in-gcp-aa529d4f3bb8

[superset-site]: https://superset.apache.org/
[docker-install-guide]: https://docs.docker.com/engine/install/
[docker-compose-install-guide]: https://docs.docker.com/compose/install/compose-plugin/#installing-compose-on-linux-systems

[local-dbt]: http://localhost:8080/
[local-airflow]: http://localhost:80801
[local-redash]: http://localhost:5000
