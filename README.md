# Torque Demo Package

The primary purpose of this package is to demonstrate the capabilities of the Torque framework — how easy it is to maintain complex cloud architectures with Torque: set up new workspaces, add new architectural components to existing workspaces, and deploy to new or existing environments. The Demo Package components, links, and providers might miss some functionality related to the ease of coding or the breadth of configuring. But, if you like how easy it is to maintain complex cloud architectures with Torque, please let us know, and we will help you get what you need in terms of functionality.

## Additional resources

- [Torque documentation](docs.torquetech.dev)
- [Torque CLI Discussion tab](https://github.com/torquetech/torque-workspace/discussions)
- [Demo Package Discussion tab](https://github.com/torquetech/torque-workspace/discussions)

## Package Content

Demo Package has the following components, links, and providers.

### Components

- [`demo/python-app`](#demopython-app): A Python deployable unit that does not expose HTTP connectivity option.
- [`demo/python-service`](#demopython-service): A Python deployable unit that exposes HTTP connectivity option. Other apps and services can connect to it and use its API.
- [`demo/postgres`](#demopostgres): PostgreSQL database instance.
- [`demo/zookeeper`](#demozookeeper): A service required by the `demo/kafka` component.
- [`demo/kafka`](#demokafka): Kafka event-steaming service (see more at https://kafka.apache.org/)
- [`demo/persistent-volume`](#demopersistent-volume): Data storage volume required in order to not get data destroyed after each deployment to either _docker-compose_ or _Kubernetes_.
- [`demo/load-balancer`](#demoload-balancer): Routes incoming traffic to services. Provides a unified external URL. Implemented by _nginx_.
- [`demo/react-app`](#demoreact-app): React application.

### Links

- [`demo/network`](#demonetwork): Provides network connectivity between the component that exposes ?.
- [`demo/psycopg`](#demopsycopg): Links a PostgreSQL database to a python-based component.
- [`demo/volume`](#demovolume): Mounts a data storage volume.
- [`demo/postgres-data`](#demopostgres-data): Mounts a data storage volume to a PostgreSQL DB component.
- [`demo/zookeeper-data`](#demozookeeper-data): Mounts a data storage volume to a Zookeeper component.
- [`demo/kafka-data`](#demokafka-data): Mounts a data storage volume to a Kafka component.
- [`demo/zookeeper-kafka`](#demozookeeper-kafka): Links a Zookeeper to a Kafka component.
- [`demo/kafka-python`](#demokafka-python): Links a Kafka to any Python-based component.
- [`demo/ingress`](#demoingress): Links ingress (_nginx_ or load balancer) to any service that exposes network interface.

### Providers

- demo/docker-compose: Generates `docker-compose.yaml` to run all components on a local development environment.
- demo/k8s: Generates Kubernetes yaml files to deploy the workspace to a Kubernetes instance.

## Prerequisites

For the `demo-package` to work properly, make sure you have the following tools installed and running in your development and CI/CD environments:

1. [Docker](https://docs.docker.com/get-docker/)
2. [docker-compose](https://docs.docker.com/compose/install/)
3. [kubectl](https://kubernetes.io/docs/tasks/tools/)
4. [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)

## Components

### demo/python-app

The Python deployable unit which does not expose HTTP connectivity option. Used for background jobs, single-use scripts, and similar. It can be linked to other components using python or network-based links.

#### Parameters

- `path` - Subdirectory where the code scaffolding will be generated. For example `path=my-app`

#### Configuration

- `development_mode` - When set to `True`, tells the component to use a Dockerfile for local development that mounts the app directory and runs the app in watch (live-reload) mode.
- `environment` - key/value dictionary of environment variables passed to the docker container.

#### Code Scaffolding

```text
.my-app
|-- app
|   `-- __init__.py
|   `-- __main__.py
|-- modules
|   `-- __init__.py
|-- Dockerfile
|-- Dockerfile.dev
|-- requirements.txt
|-- setup.py
|-- version.sh
```

There is no specific code or framework present in the `demo/python-app`. But you can imagine how we can convert it into any particular use case by extending its Python class and overriding the `on_create` method to add additional code scaffolding.

- `app` directory: Put all your code here and invoke it from the `__main__.py` file.
- `modules` directory: Used by links to put their modules and dependencies.
- `Dockerfile` file: Used by the component to generate a docker image used for Kubernetes deployment.
- `Dockerfile.dev` file: Used by the component to generate a docker image used for local development by docker-compose.
- `requirements.txt` file: List of Python package dependencies required by the python app.
- `setup.py` file: 
- `version.sh` file: Prints the app (package) version for setup.py.

#### Local Development

We recommend setting the `development_mode` flag to `True` when configuring the local development profiles. This way the component will use `Dockerfile.dev` docker image that mounts the local app directory and runs the app directly from your code.

### demo/python-service

Inherited from Python App, it is a Python deployable unit that exposes an HTTP connectivity option. Other apps and services can connect to it and use its API. Used for backend services.

#### Parameters

- `path` - Subdirectory where the code scaffolding will be generated. For example `path=my-service`

#### Configuration

- `development_mode` - When set to `True`, tells the component to use a Dockerfile for local development that mounts the app directory and runs the app in watch (live-reload) mode.
- `environment` - key/value dictionary of environment variables passed to the docker container.

#### Code Scaffolding

```text
.my-service
|-- app
|   `-- __init__.py
|   `-- __main__.py
|-- modules
|   `-- __init__.py
|-- Dockerfile
|-- Dockerfile.dev
|-- requirements.txt
|-- setup.py
|-- version.sh
```

There is no specific code or framework present in the `demo/python-service`. But you can imagine how we can convert it into any particular use case by extending its Python class and overriding the `on_create` method to add additional code scaffolding.

- `app` directory: Put all your code here and invoke it from the `__main__.py` file.
- `modules` directory: Used by links to put their modules and dependencies.
- `Dockerfile` file: Used by the component to generate a docker image used for Kubernetes deployment.
- `Dockerfile.dev` file: Used by the component to generate a docker image used for local development by docker-compose.
- `requirements.txt` file: List of Python package dependencies required by the python app.
- `setup.py` file: 
- `version.sh` file: Prints the app (package) version for setup.py.

#### Local Development

We recommend setting the `development_mode` flag to `True` when configuring the local development profiles. This way the component will use `Dockerfile.dev` docker image that mounts the local app directory and runs the service directly from your code.

### demo/postgres

PostgreSQL database instance. The demo/postgres component does not have a dedicated  directory in the workspace.

#### Configuration

- `version` - PostgreSQL version to use. Default 14.2
- `password` - A root user password.

### demo/zookeeper

According to https://zookeeper.apache.org/, ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. In the context of the Torque Demo package, ZK is required by the demo/kafka component.

This component does not have a dedicated directory in the workspace.

### demo/kafka

According to https://kafka.apache.org/, Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. In other words, a powerful, but complex piece of technology. In the context of the Torque Demo package, we wanted to show how a complex service can be simplified using when describing through a Torque component. 

This component does not have a dedicated directory in the workspace.

### demo/persistent-volume

Whenever you have a Docker container that stores data, and you want to keep that data beyond the container's lifespan (so it is not destroyed together with the container), you need to mount a persistent volume to the container. 
This component does not have a dedicated directory in the workspace.

#### Parameters

- `size` - Storage size in GB.

### demo/load-balancer

Whenever services and apps need to be accessed from the internet, or they need to know the URL that services are exposed to the internet (like react app), we need to link them to a load balancer component. 

This component does not have a dedicated directory in the workspace.

#### Configuration

- `host` - A URL where linked service components are exposed.

### demo/react-app

The `demo/react-app` code was generated using the `create-react-app` utility. It includes everything required to run the react app locally inside a docker image and then deploy it to a Kubernetes cluster.

#### Parameters

- `path` - Subdirectory where the code scaffolding will be generated. For example `path=my-app`

#### Configuration

- `development_mode` - When set to `True`, tells the component to use a Dockerfile for local development that mounts the `app` directory and runs the app in watch (reload) mode.


#### Code Scaffolding

```text
.my-service
|-- src
|   `-- App.css
|   `-- App.test.tsx
|   `-- App.tsx
|   `-- index.css
|   `-- index.tsx
|   `-- logo.svg
|-- .dockerignore
|-- .gitignore
|-- devel.sh
|-- Dockerfile
|-- Dockerfile.dev
|-- package.json
|-- package-lock.json
|-- README.md
|-- tsconfig.json
```

- `src` directory: Put all your app code here.
- `App.*`, `index.*`: Generated React App classes.
- `devel.sh`: Used by the Dockerfile.dev to run React app inside the container.
- `Dockerfile` file: Used by the component to generate a docker image used for Kubernetes deployment.
- `Dockerfile.dev` file: Used by the component to generate a docker image used for local development by docker-compose.
- `package.json` and `package-lock.json` files: Javascript package dependencies required by the React app.
- `tsconfig.json` file: TypeScript compiler configuration file.

#### Local Development

We recommend setting the `development_mode` flag to `True` when configuring the local development profiles. This way the component will use `Dockerfile.dev` docker image that mounts the local app directory and runs the app directly from your code.

## Links

### demo/network

A link that connects a service component with other services and apps. This link is used later by a provider to set up the network URL environment variable to the destination component container.

#### Destination container environment variables

- `{COMPONENT_NAME}_LINK` - a URL to the source service component.

### demo/psycopg

Extends a network link and provides a connection between a PostgresSQL database component and Python services and apps. This link adds code scaffolding for database connection and sets up required environment variables to the destination component container.

#### Destination container environment variables

- `{COMPONENT_NAME}_PSYCOPG_DB` - a PostgreSQL database name.
- `{COMPONENT_NAME}_LINK` - a URL to the PostgreSQL database instance.
- `{COMPONENT_NAME}_PSYCOPG_USER` - a PostgreSQL database user name.
- `{COMPONENT_NAME}_PSYCOPG_PASSWORD` - a PostgreSQL database user password.

### demo/volume

Components that store data usually need some form of volume mounted in order to ensure data is not lost after their service containers are restarted. The volume link sets the volume path to the destination component so a provider can correctly set up the mount point for the container.

### demo/postgres-data

Extends the demo/volume link to set the mount point as a PostgreSQL container data mount.

### demo/zookeeper-data

Extends the demo/volume link to set the mount point as a Zookeeper container data mount.

### demo/kafka-data

Extends the demo/volume link to set the mount point as a Kafka container data mount.

### demo/zookeeper-kafka

A link that connects a Zookeeper service with a Kafka service. Kafka component uses this link to set up a connection to Zookeeper.

### demo/kafka-python

A link that extends the demo/network link to connect a Kafka component with Python services and apps. This link adds code scaffolding for both Kafka producer and Kafka consumer connection. The network link part sets the environment variable to the destination component container.

### demo/ingress

A link that connects a load balancer component with a component that needs to be connected from internet. Examples are [`demo/python-service`](#demopython-service) and [`demo/react-app`](#demoreact-app).

#### Parameters

- `path` - A URL path where the service (component) will be accessible. For example, setting parameter as `path=/my-app` instructus load balancer component to route all requests coming to `https://my.domain/my-app/*` to the linked component.

#### Destination container environment variables

- `{COMPONENT_NAME}_LINK` - a URL to the Kafka instance.

## Providers

### demo/docker-compose

Generate docker-compose.yaml and execute docker compose up command to run all defined services.

### demo/k8s

Generate Kubernetes YAML files, and apply them to the connected Kubernetes cluster.
