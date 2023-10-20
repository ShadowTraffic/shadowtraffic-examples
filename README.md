# ShadowTraffic examples

This repo contains runnable examples of how to use [ShadowTraffic](http://shadowtraffic.io/) for common use cases.

Run each of these with:

```
docker run --env-file license.env -v ./<configuration file>:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --sample 10 --stdout --watch
```

- [Hello world to Postgres](hello-world-postgres.json)
- [Customers and order data](customers-orders.json)
- [Debezium change data capture](cdc.json)
- [Decodable](decodable.json)
