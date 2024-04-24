# ShadowTraffic examples

This repo contains runnable examples of how to use [ShadowTraffic](http://shadowtraffic.io/) for common use cases.

Run each of these with:

```
docker run --env-file license.env -v $(pwd)/<configuration file>:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --sample 10 --stdout --watch
```

### Hello world with Kafka

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-kafka.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-kafka%2Fdevcontainer.json)

**Discussion**

This example writes events to a Kafka topic named `testTopic`, using JSON serialization for both the key and value. This generator doesn't specify a key, so the key of the record is always null. The value is a string, which is one of three random emojis.

---

### Hello world with Postgres

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-postgres.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-postgres%2Fdevcontainer.json)

**Discussion**

This example writes events to a Postgres table named `testTable`, which has one column named `testColumn`. If this table doesn't exist when you start ShadowTraffic, it'll automatically create it for you. `testColumn` is a string, and it's value will be one of three random emojis.

---

### Hello world with S3

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-s3.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-s3%2Fdevcontainer.json)

**Discussion**

This example writes events to an S3 bucket named `testBucket`. Each object in the bucket will have the file suffix `jsonl`, and each event will be one line of JSON. Events are strings, picked by the oneOf generator that chooses a random emoji.

---

### Hello world with a webhook

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-webhook.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-webhook%2Fdevcontainer.json)

**Discussion**

This example writes events to the HTTP endpoint `https://my-site/webhook-endpoint`. The shape of the generator is determined by the connection's `dataShape`. Since it's set to `kafka`, the generator is expected to create key/value data. `dataShape` can be set to other values, which lets you decouple how your data is shaped from the webhook it's sent to.

---

### The kitchen sink: Kafka retail data

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](kafka-retail.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fkafka-retail%2Fdevcontainer.json)

**Discussion**

This example writes events to two Kafka topics: `customers` and `orders`. Events in the `customers` topic have a map value containing a few simple attributes: `customerId`, `name`, and so on.

Events in the `orders` topic have two interesting generators. First, `customerId` is generated by a `lookup` to the `customers` topic. ShadowTraffic guarantees that any `customerId`s for `orders` will have already been successfully written to the `customers` topic.

Second, `orderNumber` is defined by the `sequentialInteger` generator. This generator is stateful, so each time it generates a value, it's internal counter increases by one. You don't need to do any state management. This happens for you automatically.

---

### The kitchen sink: Postgres retail data

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](postgres-retail.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fpostgres-retail%2Fdevcontainer.json)

**Discussion**

This example writes events to two Postgres tables: `customers` and `orders`. Events in the `customers` table have a few simple columns: `customerId`, `name`, and so on.

Events in the `orders` table have two interesting generators. First, `customerId` is generated by a `lookup` to the `customers` table. ShadowTraffic guarantees that any `customerId`s for `orders` will have already been successfully written to the `customers` table.

Second, `orderNumber` is defined by the `sequentialInteger` generator. This generator is stateful, so each time it generates a value, it's internal counter increases by one. You don't need to do any state management. This happens for you automatically.

---

### The kitchen sink: S3 retail data

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](s3-retail.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fs3-retail%2Fdevcontainer.json)

**Discussion**

This example writes events to two S3 buckets: `customers` and `orders`. Events in objects of the `customers` bucket have a few simple attributes: `customerId`, `name`, and so on.

Events in objects of the `orders` bucket have two interesting generators. First, `customerId` is generated by a `lookup` to the `customers` bucket. ShadowTraffic guarantees that any `customerId`s for `orders` will have already been successfully written to the `customers` bucket.

Second, `orderNumber` is defined by the `sequentialInteger` generator. This generator is stateful, so each time it generates a value, it's internal counter increases by one. You don't need to do any state management. This happens for you automatically.

---

### Customers have a name, age, and membership level

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](basic-customer.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbasic-customer%2Fdevcontainer.json)

**Discussion**

This example generators events to a Postgres table named `customers`. The table has three rows: `name`, `age`, and `membership`.

`name` is a random full name, like John Smith.

Age is a random number between 18 and 120. By default, `uniformDistribution` generates decimal numbers. With `decimals` set to `0`, the generator instead produces integers.

`membership` is a random choice of three different levels.

---

### 57% of votes are cast for Franklin Roosevelt

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](votes.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fvotes%2Fdevcontainer.json)

**Discussion**

This example writes to a Kafka topic, with each event having a UUID key and a map value. weightedOneOf sets 57% of all candidate strings in the value to `Fraklin Roosevelt` and 43% to  `Herbert Hoover`.

---

### Transactions are uniformly priced between $2 and $200

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](transactions.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftransactions%2Fdevcontainer.json)

**Discussion**

This example writes to a Kafka topic named `transactions`, with each event having a UUID key and a map value. The value maps contain two attributes: `price` and `timestamp`. `price` is a random number between `2` and `200`, and is guaranteed to have two decimal places. `time` is the current UNIX time in milliseconds.

---

### Orders have a pre-existing customer

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](customers-orders.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcustomers-orders%2Fdevcontainer.json)

**Discussion**

This example writes to two Kafka topics, `customers` and `orders.` Events in `customers` have only a key and no value—thus, value will be `null`. Events in orders have a `customerId` which is guaranteed to have been successfully written to the `customers` topic first. The `lookup` generator targets those events and uses the `path` parameter to drill into the key's `name` attribute.

---

### Support ticket messages arrive every 5000ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](support-tickets.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsupport-tickets%2Fdevcontainer.json)

**Discussion**

This example generates events to both Kafka and Postgres.

In the first generator, straightforward events are generated to a Postgres table called `customers`. Note that because there are multiple connections, each generator has to explicitly define what connection it sends data to.

In the second generator, events are generated to a Kafka topic called `purchases`. In the value of each event, `customerId` is defined as a `lookup` to values successfully written to the `customers` table. Notice how ShadowTraffic can support lookups across connection types.

In the last generator, events are generated to a Kafka topic called `supportTickets`. This works much the same as the previous generator, but it also has a local configuration of `throttle` set. `throttle` allows this generator to only produce an event at most every `5000` milliseconds.

---

### Publish 80% of the tweets from 20% of the users

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](tweets.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftweets%2Fdevcontainer.json)

**Discussion**

This example generates data to two Kafka topics, `users` and `tweets`. In the `tweets` generator, `userId` is defined as a `lookup` to get user IDs that have been written to the `users` topic. But instead of randomly choosing previously generated user IDs, a `histogram` is used so that 20% of the user IDs will be chosen 80% of the time, and the remaining 80% of user IDs chosen 20% of the time.

This distribution holds true event as more users are generated and the pool of user IDs becomes larger.

---

### Send messages every 500 ms with a std dev of 40 ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](throttle.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fthrottle%2Fdevcontainer.json)

**Discussion**

This example generates events to a Kafka topic with on an uneven cadence. A variable is set named `delay`, which is about `500` milliseconds with a standard deviation of `40` milliseconds. Each time an event is generator, `delay` is evaluated to a new number. `delay` is then referenced to impose a throttle, and the actual value of delay is passed into outgoing `row.`

---

### Place exactly 15 orders

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](exactly.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fexactly%2Fdevcontainer.json)

**Discussion**

By default, ShadowTraffic generates events indefinitely. But in this example, setting `events exactly` to a number bounds how many events are generated. When that limited is reached, ShadowTraffic stops.

---

### Pick a date/timestamp between yesterday and tomorrow

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](time.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftime%2Fdevcontainer.json)

**Discussion**

In this example, we generate random timestamps between 24 hours into the past and 24 hours into the future—regardless of the current time. We do that by first setting a variable called `now` that captures the current wallclock time in milliseconds. Then, we create a uniformDistribution, who's lower value is now minus 24 hours and upper value is now plus 24 hours. We feed the result into `formatDateTime` to get a nice formatted string.

---

### 5 sensors whose value is the previous value plus a random number between -1 and 1

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](sensors.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsensors%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Telemetry data gets randomly delayed 10% of the time, discarded 2% of the time, and repeated 5% of the time

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](telemetry.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftelemetry%2Fdevcontainer.json)

**Discussion**

- Foo

---

### A stream of the h2o dataset configured for n=10M, k=10

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](h2o.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fh2o%2Fdevcontainer.json)

**Discussion**

- Foo

---

### An inventory of films are tracked in 100 stores, like the Sakila dataset

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](sakila.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsakila%2Fdevcontainer.json)

**Discussion**

- Foo

---

### A new user comes online every 250ms and changes their IP every 1 second

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](ip-rotation.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fip-rotation%2Fdevcontainer.json)

**Discussion**

- Foo

---

### 50 machines DDOSing EC2 instances in us-east-1 with ~200 byte packets every 10 ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](ddos.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fddos%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Suspicious accounts transacting that log in with a new IP address 1% of the time

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](fraud.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffraud%2Fdevcontainer.json)

**Discussion**

- Foo

---

### 30 JVMs report their heap readings every 250 ms which oscillate around 50 mb

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](heap-readings.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fheap-readings%2Fdevcontainer.json)

**Discussion**

- Foo

---

### 200 merchants have their businesses audited once every ~25 days

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](audits.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Faudits%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Inventory is updated every 200ms and queries check its status every 500ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](inventory-queries.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Finventory-queries%2Fdevcontainer.json)

**Discussion**

- Foo

---

### A stream of rides from New York's yellow taxi network

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](taxi-rides.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftaxi-rides%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Shopping carts add items, check out, and sometimes get abandoned

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](shopping-carts.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fshopping-carts%2Fdevcontainer.json)

**Discussion**

- Foo

---

### The Nexmark streaming benchmark of auction streams

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](nexmark.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fnexmark%2Fdevcontainer.json)

**Discussion**

- Foo

---

### 70% of all posts are from repeat users

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](repeat-users.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Frepeat-users%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Harvest customer IDs from Postgres for Kafka events

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](cross-connection.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcross-connection%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Customers go through a 4-stage funnel

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](funnel.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffunnel%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Debezium envelopes have 3 discrete states

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](cdc.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcdc%2Fdevcontainer.json)

**Discussion**

- Foo

---

### 3 support agents field phone calls, arriving once a second

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](call-center.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcall-center%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Flights take off every 5 seconds and report their geolocation

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](flights.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fflights%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Every ~2 seconds, a new game is scheduled to start with bets placed every ~500ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](bets.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbets%2Fdevcontainer.json)

**Discussion**

- Foo

---

### Bots post social content that get likes and shares only 5% of the time each

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](bots.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbots%2Fdevcontainer.json)

**Discussion**

- Foo
