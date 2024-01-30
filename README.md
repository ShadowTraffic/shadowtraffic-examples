# ShadowTraffic examples

This repo contains runnable examples of how to use [ShadowTraffic](http://shadowtraffic.io/) for common use cases.

Run each of these with:

```
docker run --env-file license.env -v $(pwd)/<configuration file>:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --sample 10 --stdout --watch
```

- First steps
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-kafka%2Fdevcontainer.json) [Hello world with Kafka](hello-world-kafka.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-progres%2Fdevcontainer.json) [Hello world with Postgres](hello-world-postgres.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-webhook%2Fdevcontainer.json) [Hello world with a webhook](hello-world-webhook.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fdecodable%2Fdevcontainer.json) [Hello world to Decodable](decodable.json)
- Basic examples
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbasic-consumer%2Fdevcontainer.json) [Customers have a name, age, and membership level](basic-customer.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fvotes%2Fdevcontainer.json) [57% of votes are cast for Franklin Roosevelt](votes.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftransactions%2Fdevcontainer.json) [Transactions are uniformly priced between $2 and $200](transactions.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcustomers-orders%2Fdevcontainer.json) [Orders have a pre-existing customer](customers-orders.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsupport-tickets%2Fdevcontainer.json) [Support ticket messages arrive every 5000ms](support-tickets.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftweets%2Fdevcontainer.json) [Publish 80% of the tweets from 20% of the users](tweets.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fthrottle%2Fdevcontainer.json) [Send messages every 500 ms with a std dev of 40 ms](throttle.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fexactly%2Fdevcontainer.json) [Place exactly 15 orders](exactly.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftime%2Fdevcontainer.json) [Pick a date/timestamp between yesterday and tomorrow](time.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fheap-readings%2Fdevcontainer.json) [3 JVMs reporting their heap sizes which oscillate between 150 and 3000 megabytes](heap-readings.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsensors%2Fdevcontainer.json) [5 sensors whose value is the previous value plus a random number between -1 and 1](sensors.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftelemetry%2Fdevcontainer.json) [Telemetry data gets randomly delayed 10% of the time, discarded 2% of the time, and repeated 5% of the time](telemetry.json)
- Advanced examples
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Frepeat-users%2Fdevcontainer.json) [70% of all posts are from repeat users](repeat-users.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcross-connection%2Fdevcontainer.json) [Harvest customer IDs from Postgres for Kafka events](cross-connection.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffunnel%2Fdevcontainer.json)l [Customers go through a 4-stage funnel](funnel.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcdc%2Fdevcontainer.json) [Debezium envelopes have 3 discrete states](cdc.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcall-center%2Fdevcontainer.json) [3 support agents field phone calls, arriving once a second](call-center.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fflights%2Fdevcontainer.json) [Flights take off every 5 seconds and report their geolocation](flights.json)