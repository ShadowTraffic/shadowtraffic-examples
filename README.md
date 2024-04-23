# ShadowTraffic examples

This repo contains runnable examples of how to use [ShadowTraffic](http://shadowtraffic.io/) for common use cases.

Run each of these with:

```
docker run --env-file license.env -v $(pwd)/<configuration file>:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --sample 10 --stdout --watch
```

### Hello world with Kafka

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-kafka%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-kafka.json)

**How it works:**

- Writes data to [Kafka](https://docs.shadowtraffic.io/reference/connections/kafka/) using JSON serialization for both the key and value. The value is the output of [oneOf](https://docs.shadowtraffic.io/reference/generators/oneOf/), which picks one of three emojis at random.

---

### Hello world with Postgres

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-postgres%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-postgres.json)

**How it works:**

- One connection, `pg`, writes data to a single table with a single column. Auto creates the table for you if it doesn't exist.

---

### Hello world with S3

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-s3%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-s3.json)

**How it works:**

- Writes objects to S3 with a jsonl file suffix, one line at a time.

---

### Hello world with a webhook

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fhello-world-webhook%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](hello-world-webhook.json)

**How it works:**

- The generator gets shaped on `dataShape`.

---

### Hello world to Decodable

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fdecodable%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](decodable.json)

**How it works:**

- Pass through auth details in connection.
- All data has to go through the value.

---

### The kitchen sink: Kafka retail data

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fkafka-retail%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](kafka-retail.json)

**How it works:**

- Foo

---

### The kitchen sink: Postgres retail data

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fpostgres-retail%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](postgres-retail.json)

**How it works:**

- Foo

---

### The kitchen sink: S3 retail data

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fs3-retail%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](s3-retail.json)

**How it works:**

- Foo

---

### Customers have a name, age, and membership level

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbasic-customer%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](basic-customer.json)

**How it works:**

- Foo

---

### 57% of votes are cast for Franklin Roosevelt

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fvotes%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](votes.json)

**How it works:**

- Foo

---

### Transactions are uniformly priced between $2 and $200

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftransactions%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](transactions.json)

**How it works:**

- Foo

---

### Orders have a pre-existing customer

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcustomers-orders%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](customers-orders.json)

**How it works:**

- Foo

---

### Support ticket messages arrive every 5000ms

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsupport-tickets%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](support-tickets.json)

**How it works:**

- Foo

---

### Publish 80% of the tweets from 20% of the users

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftweets%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](tweets.json)

**How it works:**

- Foo

---

### Send messages every 500 ms with a std dev of 40 ms

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fthrottle%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](throttle.json)

**How it works:**

- Foo

---

### Place exactly 15 orders

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fexactly%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](exactly.json)

**How it works:**

- Foo

---

### Pick a date/timestamp between yesterday and tomorrow

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftime%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](time.json)

**How it works:**

- Foo

---

### 5 sensors whose value is the previous value plus a random number between -1 and 1

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsensors%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](sensors.json)

**How it works:**

- Foo

---

### Telemetry data gets randomly delayed 10% of the time, discarded 2% of the time, and repeated 5% of the time

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftelemetry%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](telemetry.json)

**How it works:**

- Foo

---

### A stream of the h2o dataset configured for n=10M, k=10

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fh2o%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](h2o.json)

**How it works:**

- Foo

---

### An inventory of films are tracked in 100 stores, like the Sakila dataset

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fsakila%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](sakila.json)

**How it works:**

- Foo

---

### A new user comes online every 250ms and changes their IP every 1 second

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fip-rotation%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](ip-rotation.json)

**How it works:**

- Foo

---

### 50 machines DDOSing EC2 instances in us-east-1 with ~200 byte packets every 10 ms

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fddos%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](ddos.json)

**How it works:**

- Foo

---

### Suspicious accounts transacting that log in with a new IP address 1% of the time

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffraud%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](fraud.json)

**How it works:**

- Foo

---

### 30 JVMs report their heap readings every 250 ms which oscillate around 50 mb

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fheap-readings%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](heap-readings.json)

**How it works:**

- Foo

---

### 200 merchants have their businesses audited once every ~25 days

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Faudits%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](audits.json)

**How it works:**

- Foo

---

### Inventory is updated every 200ms and queries check its status every 500ms

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Finventory-queries%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](inventory-queries.json)

**How it works:**

- Foo

---

### A stream of rides from New York's yellow taxi network

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ftaxi-rides%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](taxi-rides.json)

**How it works:**

- Foo

---

### Shopping carts add items, check out, and sometimes get abandoned

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fshopping-carts%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](shopping-carts.json)

**How it works:**

- Foo

---

### The Nexmark streaming benchmark of auction streams

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fnexmark%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](nexmark.json)

**How it works:**

- Foo

---

### 70% of all posts are from repeat users

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Frepeat-users%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](repeat-users.json)

**How it works:**

- Foo

---

### Harvest customer IDs from Postgres for Kafka events

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcross-connection%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](cross-connection.json)

**How it works:**

- Foo

---

### Customers go through a 4-stage funnel

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Ffunnel%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](funnel.json)

**How it works:**

- Foo

---

### Debezium envelopes have 3 discrete states

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcdc%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](cdc.json)

**How it works:**

- Foo

---

### 3 support agents field phone calls, arriving once a second

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fcall-center%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](call-center.json)

**How it works:**

- Foo

---

### Flights take off every 5 seconds and report their geolocation

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fflights%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](flights.json)

**How it works:**

- Foo

---

### Every ~2 seconds, a new game is scheduled to start with bets placed every ~500ms

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbets%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](bets.json)

**How it works:**

- Foo

---

### Bots post social content that get likes and shares only 5% of the time each

[![Demo](https://img.shields.io/badge/demo-🚀-%2396b939)](https://github.com/codespaces/new?machine=basicLinux32gb&repo=707805347&ref=main&devcontainer_path=.devcontainer%2Fbots%2Fdevcontainer.json)
[![Demo](https://img.shields.io/badge/config-🎁-%2339b9aa)](bots.json)

**How it works:**

- Foo
