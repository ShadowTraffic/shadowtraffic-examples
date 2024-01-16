# ShadowTraffic examples

This repo contains runnable examples of how to use [ShadowTraffic](http://shadowtraffic.io/) for common use cases.

Run each of these with:

```
docker run --env-file license.env -v $(pwd)/<configuration file>:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --sample 10 --stdout --watch
```

- First steps
    - [Hello world with Kafka](hello-world-kafka.json)
    - [Hello world with Postgres](hello-world-postgres.json)
    - [Hello world with a webhook](hello-world-webhook.json)
    - [Hello world to Decodable](decodable.json)
- Basic examples
    - [Customers have a name, age, and membership level](basic-customer.json)
    - [57% of votes are cast for Franklin Roosevelt](votes.json)
    - [Transactions are uniformly priced between $2 and $200](transactions.json)
    - [Orders have a pre-existing customer](customers-orders.json)
    - [Support ticket messages arrive every 5000ms](support-tickets.json)
    - [Publish 80% of the tweets from 20% of the users](tweets.json)
    - [Send messages every 500 ms with a std dev of 40 ms](throttle.json)
    - [Place exactly 15 orders](exactly.json)
    - [Pick a date/timestamp between yesterday and tomorrow](time.json)
    - [3 JVMs reporting their heap sizes which oscillate between 150 and 3000 megabytes](heap-readings.json)
    - [5 sensors whose value is the previous value plus a random number between -1 and 1](sensors.json)
    - [Telemetry data gets randomly delayed 10% of the time, discarded 2% of the time, and repeated 5% of the time](telemetry.json)
- Advanced examples
    - [70% of all posts are from repeat users](repeat-users.json)
    - [Harvest customer IDs from Postgres for Kafka events](cross-connection.json)
    - [Customers go through a 4-stage funnel](funnel.json)
    - [Debezium envelopes have 3 discrete states](cdc.json)
    - [3 support agents field phone calls, arriving once a second](call-center.json)
    - [Flights take off every 5 seconds and report their geolocation](flights.json)