# ShadowTraffic examples

This repo contains runnable examples of how to use [ShadowTraffic](http://shadowtraffic.io/) for common use cases.

Run each of these with:

```
docker run --env-file license.env -v $(pwd)/<configuration file>:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --sample 10 --stdout --watch
```

* [Hello world with Kafka](#hello-world-with-kafka)
* [Hello world with Postgres](#hello-world-with-postgres)
* [Hello world with S3](#hello-world-with-s3)
* [Hello world with a webhook](#hello-world-with-a-webhook)
* [The kitchen sink: Kafka retail data](#the-kitchen-sink-kafka-retail-data)
* [The kitchen sink: Postgres retail data](#the-kitchen-sink-postgres-retail-data)
* [The kitchen sink: S3 retail data](#the-kitchen-sink-s3-retail-data)
* [Customers have a name, age, and membership level](#customers-have-a-name-age-and-membership-level)
* [57% of votes are cast for Franklin Roosevelt](#57-of-votes-are-cast-for-franklin-roosevelt)
* [Transactions are uniformly priced between $2 and $200](#transactions-are-uniformly-priced-between-2-and-200)
* [Orders have a pre-existing customer](#orders-have-a-pre-existing-customer)
* [Support ticket messages arrive every 5000ms](#support-ticket-messages-arrive-every-5000ms)
* [Publish 80% of the tweets from 20% of the users](#publish-80-of-the-tweets-from-20-of-the-users)
* [Send messages every 500 ms with a std dev of 40 ms](#send-messages-every-500-ms-with-a-std-dev-of-40-ms)
* [Place exactly 15 orders](#place-exactly-15-orders)
* [Pick a date/timestamp between yesterday and tomorrow](#pick-a-datetimestamp-between-yesterday-and-tomorrow)
* [5 sensors whose value is the previous value plus a random number between -1 and 1](#5-sensors-whose-value-is-the-previous-value-plus-a-random-number-between--1-and-1)
* [Telemetry data gets randomly delayed 10% of the time, discarded 2% of the time, and repeated 5% of the time](#telemetry-data-gets-randomly-delayed-10-of-the-time-discarded-2-of-the-time-and-repeated-5-of-the-time)
* [A stream of the h2o dataset configured for n=10M, k=10](#a-stream-of-the-h2o-dataset-configured-for-n10m-k10)
* [An inventory of films are tracked in 100 stores, like the Sakila dataset](#an-inventory-of-films-are-tracked-in-100-stores-like-the-sakila-dataset)
* [A new user comes online every 250ms and changes their IP every 1 second](#a-new-user-comes-online-every-250ms-and-changes-their-ip-every-1-second)
* [50 machines DDOSing EC2 instances in us-east-1 with ~200 byte packets every 10 ms](#50-machines-ddosing-ec2-instances-in-us-east-1-with-200-byte-packets-every-10-ms)
* [Suspicious accounts transacting that log in with a new IP address 1% of the time](#suspicious-accounts-transacting-that-log-in-with-a-new-ip-address-1-of-the-time)
* [30 JVMs report their heap readings every 250 ms which oscillate around 50 mb](#30-jvms-report-their-heap-readings-every-250-ms-which-oscillate-around-50-mb)
* [200 merchants have their businesses audited once every ~25 days](#200-merchants-have-their-businesses-audited-once-every-25-days)
* [Inventory is updated every 200ms and queries check its status every 500ms](#inventory-is-updated-every-200ms-and-queries-check-its-status-every-500ms)
* [A stream of rides from New York's yellow taxi network](#a-stream-of-rides-from-new-yorks-yellow-taxi-network)
* [Shopping carts add items, check out, and sometimes get abandoned](#shopping-carts-add-items-check-out-and-sometimes-get-abandoned)
* [The Nexmark streaming benchmark of auction streams](#the-nexmark-streaming-benchmark-of-auction-streams)
* [70% of all posts are from repeat users](#70-of-all-posts-are-from-repeat-users)
* [Harvest customer IDs from Postgres for Kafka events](#harvest-customer-ids-from-postgres-for-kafka-events)
* [Customers go through a 4-stage funnel](#customers-go-through-a-4-stage-funnel)
* [Debezium envelopes have 3 discrete states](#debezium-envelopes-have-3-discrete-states)
* [3 support agents field phone calls, arriving once a second](#3-support-agents-field-phone-calls-arriving-once-a-second)
* [Flights take off every 5 seconds and report their geolocation](#flights-take-off-every-5-seconds-and-report-their-geolocation)
* [Every ~2 seconds, a new game is scheduled to start with bets placed every ~500ms](#every-2-seconds-a-new-game-is-scheduled-to-start-with-bets-placed-every-500ms)
* [Bots post social content that get likes and shares only 5% of the time each](#bots-post-social-content-that-get-likes-and-shares-only-5-of-the-time-each)
* [Latency is about 10 milliseconds, with bursts to 50 and 150 every 2 and 5 minutes](#latency-is-about-10-milliseconds-with-bursts-to-50-and-150-every-2-and-5-minutes)
* [A server transitions between healthcheck statuses every 15 seconds](#a-server-transitions-between-healthcheck-statuses-every-15-seconds)
* [A client emits OTEL telemetry data](#a-client-emits-otel-telemetry-data)
* [The Northwind data set](#the-northwind-data-set)
### 

### Hello world with Kafka

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-kafka.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-kafka%2Fdevcontainer.json)

**Discussion**

This example writes events to a [Kafka](https://docs.shadowtraffic.io/connections/kafka/) topic named `testTopic`, using JSON serialization for both the key and value. This generator doesn't specify a key, so the key of the record is always null. The value is a string, which is [one of](https://docs.shadowtraffic.io/functions/oneOf/) three random emojis.

---

### Hello world with Postgres

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-postgres.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-postgres%2Fdevcontainer.json)

**Discussion**

This example writes events to a [Postgres](https://docs.shadowtraffic.io/connections/postgres/) table named `testTable`, which has one column named `testColumn`. If the table doesn't exist when you start ShadowTraffic, it'll automatically create it for you. `testColumn` is a string, and it's value will be [one of](https://docs.shadowtraffic.io/functions/oneOf/) three random emojis.

---

### Hello world with S3

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-s3.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-s3%2Fdevcontainer.json)

**Discussion**

This example writes events to an [S3](https://docs.shadowtraffic.io/connections/s3/) bucket named `testBucket`. Each object in the bucket will have the file suffix `.jsonl`, and each event will be one line of JSON. Events are strings, picked by the [oneOf](https://docs.shadowtraffic.io/functions/oneOf/) generator that chooses a random emoji.

---

### Hello world with a webhook

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-webhook.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-webhook%2Fdevcontainer.json)

**Discussion**

This example writes events to the [HTTP endpoint](https://docs.shadowtraffic.io/connections/webhook/) `https://my-site/webhook-endpoint`. Not much commentary needed!

---

### The kitchen sink: Kafka retail data

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](kafka-retail.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fkafka-retail%2Fdevcontainer.json)

**Discussion**

This example writes events to two Kafka topics: `customers` and `orders`. Events in the `customers` topic have a map value containing a few simple attributes: `customerId`, `name`, and so on.

Events in the `orders` topic have two interesting generators. First, `customerId` is generated by a [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) to the `customers` topic. ShadowTraffic guarantees that any `customerId`s for `orders` will have already been successfully written to the `customers` topic.

Second, `orderNumber` is defined by the [`sequentialInteger`](https://docs.shadowtraffic.io/functions/sequentialInteger/) generator. This generator is stateful, so each time it generates a value, its internal counter increases by one. You don't need to do any state management. This happens for you automatically.

---

### The kitchen sink: Postgres retail data

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](postgres-retail.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fpostgres-retail%2Fdevcontainer.json)

**Discussion**

This example writes events to two Postgres tables: `customers` and `orders`. Events in the `customers` table have a few simple columns: `customerId`, `name`, and so on.

Events in the `orders` table have two interesting generators. First, `customerId` is generated by a [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) to the `customers` table. ShadowTraffic guarantees that any `customerId`s for `orders` will have already been successfully written to the `customers` table.

Second, `orderNumber` is defined by the [`sequentialInteger`](https://docs.shadowtraffic.io/functions/sequentialInteger/) generator. This generator is stateful, so each time it generates a value, it's internal counter increases by one. You don't need to do any state management. This happens for you automatically.

---

### The kitchen sink: S3 retail data

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](s3-retail.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fs3-retail%2Fdevcontainer.json)

**Discussion**

This example writes events to two S3 buckets: `customers` and `orders`. Events in objects of the `customers` bucket have a few simple attributes: `customerId`, `name`, and so on.

Events in objects of the `orders` bucket have two interesting generators. First, `customerId` is generated by a [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) to the `customers` bucket. ShadowTraffic guarantees that any `customerId`s for `orders` will have already been successfully written to the `customers` bucket.

Second, `orderNumber` is defined by the [`sequentialInteger`](https://docs.shadowtraffic.io/functions/sequentialInteger/) generator. This generator is stateful, so each time it generates a value, it's internal counter increases by one. You don't need to do any state management. This happens for you automatically.

---

### Customers have a name, age, and membership level

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](basic-customer.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbasic-customer%2Fdevcontainer.json)

**Discussion**

This example generates events to a Postgres table named `customers`. The table has three columns: `name`, `age`, and `membership`.

`name` is a random full name, like John Smith.

Age is a random number between 18 and 120. By default, `uniformDistribution` generates decimal numbers. With `decimals` set to `0`, the generator instead produces integers.

`membership` is a random choice of three different levels.

---

### 57% of votes are cast for Franklin Roosevelt

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](votes.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fvotes%2Fdevcontainer.json)

**Discussion**

This example writes to a Kafka topic, with each event having a UUID key and a map value. `weightedOneOf` sets 57% of all candidate strings in the value to `Fraklin Roosevelt` and 43% to  `Herbert Hoover`.

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

This example writes to two Kafka topics, `customers` and `orders.` Events in `customers` have only a key and no value—thus, value will be `null`. Events in orders have a `customerId` which is guaranteed to have been successfully written to the `customers` topic first. The [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) generator targets those events and uses the `path` parameter to drill into the key's `name` attribute.

---

### Support ticket messages arrive every 5000ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](support-tickets.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsupport-tickets%2Fdevcontainer.json)

**Discussion**

This example generates events to both Kafka and Postgres.

In the first generator, straightforward events are generated to a Postgres table called `customers`. Note that because there are multiple connections, each generator has to explicitly define what connection it sends data to.

In the second generator, events are generated to a Kafka topic called `purchases`. In the value of each event, `customerId` is defined as a [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) to values successfully written to the `customers` table. Notice how ShadowTraffic can support lookups across connection types.

In the last generator, events are generated to a Kafka topic called `supportTickets`. This works much the same as the previous generator, but it also has a local configuration of `throttleMs` set. `throttleMs` allows this generator to only produce an event at most every `5000` milliseconds.

---

### Publish 80% of the tweets from 20% of the users

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](tweets.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftweets%2Fdevcontainer.json)

**Discussion**

This example generates data to two Kafka topics, `users` and `tweets`. In the `tweets` generator, `userId` is defined as a [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) to get user IDs that have been written to the `users` topic. But instead of randomly choosing previously generated user IDs, a `histogram` is used so that 20% of the user IDs will be chosen 80% of the time, and the remaining 80% of user IDs chosen 20% of the time.

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

By default, ShadowTraffic generates events indefinitely. But in this example, setting `maxEvents` to a number bounds how many events are generated. When that limited is reached, ShadowTraffic stops.

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

This example models different sensors whose previous reading influences its next reading. There are a few parts to this one.

First, each event has a `timestamp`, set in the row, that will be part of every generated event.

Second, a [`stateMachine`](https://docs.shadowtraffic.io/functions/stateMachine/) is used to model each sensor's readings over time. In the `start` state, each sensor's initial value is set to roughly `50.` In the `update` state, which it indefinitely stays in, the reading is set by adding the previous value with a random value between `-1` and `1`.

Lastly, to model many sensors, and not just one, [`fork`](https://docs.shadowtraffic.io/overview/#forks) is used to spawn `5` simultaneous generators, each of which is spun up `250` milliseconds after the previous to make their updates stagger. A special variable called `forkKey` becomes available so that each generator can know what fork it represents—in this case, that means which sensor it is.

---

### Telemetry data gets randomly delayed 10% of the time, discarded 2% of the time, and repeated 5% of the time

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](telemetry.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftelemetry%2Fdevcontainer.json)

**Discussion**

This example generates data to a Kafka topic, but uses a few parameters to warp the data:

1. `10%` of the data is [delayed](https://docs.shadowtraffic.io/generator-configuration/delay/) from being sent out by `200 - 800` milliseconds.
2. `2%` of the data is completely [discarded](https://docs.shadowtraffic.io/generator-configuration/discard/) and never gets sent to the topic.
3. `5%` of the data is [repeated](https://docs.shadowtraffic.io/generator-configuration/repeat/) twice.

All of these parameters compose, so it's conceivable that an event is repeated, with one repetition getting delayed and another getting dropped.

---

### A stream of the h2o dataset configured for n=10M, k=10

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](h2o.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fh2o%2Fdevcontainer.json)

**Discussion**

This example generates streaming data to match the popular [h2o data set](https://taeinkwon.com/projects/h2o/). Nothing especially exotic about this one.

---

### An inventory of films are tracked in 100 stores, like the Sakila dataset

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](sakila.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsakila%2Fdevcontainer.json)

**Discussion**

This example generates data to mimic a subset of the [Sakila data set](https://dev.mysql.com/doc/sakila/en/).

In the first generator, 100 forks are created to mimic 100 different stores who sell movies. The second generator, `inventory` does a [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) into each store ID and periodically modifies its available movies.

---

### A new user comes online every 250ms and changes their IP every 1 second

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](ip-rotation.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fip-rotation%2Fdevcontainer.json)

**Discussion**

This example simulates events being written to a Postgres table. By contrast to other examples, this generator not only inserts rows, but also updates and deletes rows.

This generator uses a [state machine](https://docs.shadowtraffic.io/functions/stateMachine/) to track whether a row has been initial written, and whether it's eligible to be updated or deleted. By setting the `op` key on the generator, you can change whether the event should be treated as an insert, update, or delete.

This generator uses `varsOnce` to lock each users email so that it will never change.

`stagger` is used in the [`fork`](https://docs.shadowtraffic.io/overview/#forks) section so that each new user will apparently come online every `250` milliseconds after the previous.

---

### 50 machines DDOSing EC2 instances in us-east-1 with ~200 byte packets every 10 ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](ddos.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fddos%2Fdevcontainer.json)

**Discussion**

This example simulates `50` machines sending packets to a Kafka topic.

By setting `maxForks` to `50`, this generator will be spawn parallel instances and stop when it reaches `50`. To differentiate which machine is sending packets, `sourceIP` is set to the special variable `forKey`, which represents the currently running fork.

---

### Suspicious accounts transacting that log in with a new IP address 1% of the time

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](fraud.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffraud%2Fdevcontainer.json)

**Discussion**

This example simulates that a small percentage of the time, a suspicious login happens, which is defined by a login with a new IP address.

By using `varsOnce`, each user is assigned a one-time IP address. But composing that with `weightedOne`, 99% of the time that pre-determined IP address is chosen, and 1% of the time a new address is fabricated on the spot.

---

### 30 JVMs report their heap readings every 250 ms which oscillate around 50 mb

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](heap-readings.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fheap-readings%2Fdevcontainer.json)

**Discussion**

This example simulates `30` individual JVMs reporting their metrics. [`fork`](https://docs.shadowtraffic.io/overview/#forks) is used to create the `30` instances, who's keys are defined by strings like `jvm-1`, `jvm-2`, etc through [`sequentialStrings`](https://docs.shadowtraffic.io/functions/sequentialString/).

A [state machine](https://docs.shadowtraffic.io/functions/stateMachine/) is used to calculate its `heapSize` as its previous value plus a random number between `-1` and `1`.

---

### 200 merchants have their businesses audited once every ~25 days

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](audits.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Faudits%2Fdevcontainer.json)

**Discussion**

This example uses statistical distributions with large numbers to simulate infrequently occurring events. In the `audits` generator, `auditDate` is set to `now` minus a number of days. In the `throttleMs`, a similar approach is used to make sure this generator doesn't run for a number of days after.

---

### Inventory is updated every 200ms and queries check its status every 500ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](inventory-queries.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Finventory-queries%2Fdevcontainer.json)

**Discussion**

This example uses two generators, with the second only being allowed to run every `500` milliseconds according to its throttle value. [`sequentialStrings`](https://docs.shadowtraffic.io/reference/generators/sequentialString/) and [`sequentialInteger`](https://docs.shadowtraffic.io/functions/sequentialInteger/) are used in the first generator to create stateful sequences of data.

---

### A stream of rides from New York's yellow taxi network

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](taxi-rides.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftaxi-rides%2Fdevcontainer.json)

**Discussion**

This example mimics a streaming version of the [New York City taxi data set](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Most of the generator is simple, but the `total_amount` is a derived column that requires adding a bunch of other columns together.

---

### Shopping carts add items, check out, and sometimes get abandoned

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](shopping-carts.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fshopping-carts%2Fdevcontainer.json)

**Discussion**

This example generates shopping cart events, some of which get cancelled and never check out. By supplying no transition for a state in the `transitions` key of the [state machine](https://docs.shadowtraffic.io/functions/stateMachine/), `CHECKED_OUT` and `CANCELLED` are treated as terminal states.

---

### The Nexmark streaming benchmark of auction streams

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](nexmark.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fnexmark%2Fdevcontainer.json)

**Discussion**

This example generates data similar to the [Nexmark benchmark input data](https://github.com/nexmark/nexmark). Specifically, it's modeled after the Flink input example.

---

### 70% of all posts are from repeat users

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](repeat-users.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Frepeat-users%2Fdevcontainer.json)

**Discussion**

This example does a self-lookup. When you do a self-lookup, you need to allow some percentage of the time to generate values, which is why there's a `weightedOneOf` generator. If there wasn't, ShadowTraffic could never generate an initial value, and there would be nothing to look up.

---

### Harvest customer IDs from Postgres for Kafka events

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](cross-connection.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcross-connection%2Fdevcontainer.json)

**Discussion**

This example generates events to both Kafka and Postgres. Notice how [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) can work across connections. When you have multiple connections, you must specify which connection each generator should send data to, as denoted by the `connection` attribute.

---

### Customers go through a 4-stage funnel

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](funnel.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffunnel%2Fdevcontainer.json)

**Discussion**

This example uses a [state machine](https://docs.shadowtraffic.io/functions/stateMachine/) to simulate customers moving through different states on a website. Notice how in `transitions`, a `oneOf` generator can be used to dynamically pick the next state.

---

### Debezium envelopes have 3 discrete states

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](cdc.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcdc%2Fdevcontainer.json)

**Discussion**

This example models Debezium change data capture envelopes. It uses a [state machine](https://docs.shadowtraffic.io/functions/stateMachine/) to track whether a row is inserted for the first time, updated, or deleted.

Debezium objects show you how an entire object has changed, in both before and after states, so simulating it requires remembering previously generated data. This example uses two ways to do that:

1. The state machine is configured with `"merge": { "previous": true }` so that the previous event will be deep merged into the current.
2. The `previousEvent` generator to accesses the last values and swaps the `before` and `after` states.

---

### 3 support agents field phone calls, arriving once a second

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](call-center.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcall-center%2Fdevcontainer.json)

**Discussion**

This example creates exactly 3 support agent events, and an indefinite number of call events.

Notice how `calls` uses [`fork`](https://docs.shadowtraffic.io/overview/#forks) and a [`lookup`](https://docs.shadowtraffic.io/functions/lookup/) for its key. In forks, `key` must be unique, so this has the effect that each agent can only field one call at a time. If two forks are spawned with the same key, the newer one will be stopped from launching.

---

### Flights take off every 5 seconds and report their geolocation

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](flights.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fflights%2Fdevcontainer.json)

**Discussion**

This example simulates random flight paths between different geolocations. [`waypoints`](https://docs.shadowtraffic.io/functions/waypoints/) computes the steps between the coordinates, and repeated calls serve them up one at a time.

---

### Every ~2 seconds, a new game is scheduled to start with bets placed every ~500ms

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](bets.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbets%2Fdevcontainer.json)

**Discussion**

This example creates a [`fork`](https://docs.shadowtraffic.io/overview/#forks) per game, where each game moves through different states of completion. Each game is scheduled about `2000` milliseconds after the previous, with some jitter created by the `normalDistribution` generator.

---

### Bots post social content that get likes and shares only 5% of the time each

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](bots.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbots%2Fdevcontainer.json)

**Discussion**

This example uses a [state machine](https://docs.shadowtraffic.io/functions/stateMachine/) to weight the activity of a social media post. Most posts don't get much traffic; some a lot of traffic; others a lot of spam. This example uses `merge previous` to automatically merge in previous activity.

---

### Latency is about 10 milliseconds, with bursts to 50 and 150 every 2 and 5 minutes

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](latency-readings.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Flatency-readings%2Fdevcontainer.json)

**Discussion**

This example uses the [`intervals`](https://docs.shadowtraffic.io/functions/intervals/) function to change how the generator behaves over time. When the wallclock time reaches the 5th minute, the latency shifts from 10 to 150. When it reaches the 2nd minute, it shifts to 50. Notice how some wallclock values, like 10:20 AM, are divisible by both 5 and 2. `intervals` is evaluated in priority order, so in this case the burst to 150 takes priority because it's listed first.

---

### A server transitions between healthcheck statuses every 15 seconds

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](healthcheck.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhealthcheck%2Fdevcontainer.json)

**Discussion**

This example uses a [state machine](https://docs.shadowtraffic.io/functions/stateMachine/) to weight the probability of a server transitioning from ok, to warn, to bad. The next status mostly resembles the previous one.

---

### A client emits OTEL telemetry data

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](otel.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fotel%2Fdevcontainer.json)

**Discussion**

A reference implementation to generate minimal Open Telemetry events.

---

### The Northwind data set

[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](northwind.json)
[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fnorthwind%2Fdevcontainer.json)

**Discussion**

A reference configuration to generate an indefinite amount of [Northwind data]() to MotherDuck.