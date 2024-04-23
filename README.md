# ShadowTraffic examples

This repo contains runnable examples of how to use [ShadowTraffic](http://shadowtraffic.io/) for common use cases.

Run each of these with:

```
docker run --env-file license.env -v $(pwd)/<configuration file>:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --sample 10 --stdout --watch
```

### Hello world with Kafka

[![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-kafka%2Fdevcontainer.json)

Lorem ipsum



- First steps
    -  [Hello world with Kafka](hello-world-kafka.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-postgres%2Fdevcontainer.json) [Hello world with Postgres](hello-world-postgres.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-s3%2Fdevcontainer.json) [Hello world with S3](hello-world-s3.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-webhook%2Fdevcontainer.json) [Hello world with a webhook](hello-world-webhook.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fdecodable%2Fdevcontainer.json) [Hello world to Decodable](decodable.json)
- Basic examples
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fkafka-retail%2Fdevcontainer.json) [The kitchen sink: Kafka retail data](kafka-retail.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fpostgres-retail%2Fdevcontainer.json) [The kitchen sink: Postgres retail data](postgres-retail.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fs3-retail%2Fdevcontainer.json) [The kitchen sink: S3 retail data](s3-retail.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbasic-customer%2Fdevcontainer.json) [Customers have a name, age, and membership level](basic-customer.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fvotes%2Fdevcontainer.json) [57% of votes are cast for Franklin Roosevelt](votes.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftransactions%2Fdevcontainer.json) [Transactions are uniformly priced between $2 and $200](transactions.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcustomers-orders%2Fdevcontainer.json) [Orders have a pre-existing customer](customers-orders.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsupport-tickets%2Fdevcontainer.json) [Support ticket messages arrive every 5000ms](support-tickets.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftweets%2Fdevcontainer.json) [Publish 80% of the tweets from 20% of the users](tweets.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fthrottle%2Fdevcontainer.json) [Send messages every 500 ms with a std dev of 40 ms](throttle.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fexactly%2Fdevcontainer.json) [Place exactly 15 orders](exactly.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftime%2Fdevcontainer.json) [Pick a date/timestamp between yesterday and tomorrow](time.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsensors%2Fdevcontainer.json) [5 sensors whose value is the previous value plus a random number between -1 and 1](sensors.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftelemetry%2Fdevcontainer.json) [Telemetry data gets randomly delayed 10% of the time, discarded 2% of the time, and repeated 5% of the time](telemetry.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fh2o%2Fdevcontainer.json) [A stream of the h2o dataset configured for n=10M, k=10](h2o.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsakila%2Fdevcontainer.json) [An inventory of films are tracked in 100 stores, like the Sakila dataset](sakila.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fip-rotation%2Fdevcontainer.json) [A new user comes online every 250ms and changes their IP every 1 second](ip-rotation.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fddos%2Fdevcontainer.json) [50 machines DDOSing EC2 instances in us-east-1 with ~200 byte packets every 10 ms](ddos.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffraud%2Fdevcontainer.json) [Suspicious accounts transacting that log in with a new IP address 1% of the time](fraud.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fheap-readings%2Fdevcontainer.json) [30 JVMs report their heap readings every 250 ms which oscillate around 50 mb](heap-readings.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Faudits%2Fdevcontainer.json) [200 merchants have their businesses audited once every ~25 days](audits.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Finventory-queries%2Fdevcontainer.json) [Inventory is updated every 200ms and queries check its status every 500ms](inventory-queries.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftaxi-rides%2Fdevcontainer.json) [A stream of rides from New York's yellow taxi network](taxi-rides.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fshopping-carts%2Fdevcontainer.json) [Shopping carts add items, check out, and sometimes get abandoned](shopping-carts.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fnexmark%2Fdevcontainer.json) [The Nexmark streaming benchmark of auction streams](nexmark.json)
- Advanced examples
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Frepeat-users%2Fdevcontainer.json) [70% of all posts are from repeat users](repeat-users.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcross-connection%2Fdevcontainer.json) [Harvest customer IDs from Postgres for Kafka events](cross-connection.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffunnel%2Fdevcontainer.json) [Customers go through a 4-stage funnel](funnel.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcdc%2Fdevcontainer.json) [Debezium envelopes have 3 discrete states](cdc.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcall-center%2Fdevcontainer.json) [3 support agents field phone calls, arriving once a second](call-center.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fflights%2Fdevcontainer.json) [Flights take off every 5 seconds and report their geolocation](flights.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbets%2Fdevcontainer.json) [Every ~2 seconds, a new game is scheduled to start with bets placed every ~500ms](bets.json)
    - [![Demo](https://img.shields.io/badge/demo-%F0%9F%9A%80-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbots%2Fdevcontainer.json) [Bots post social content that get likes and shares only 5% of the time each](bots.json)
