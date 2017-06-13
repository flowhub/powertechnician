# powertechnician

Electricity consumption forecasts for a changing climate. Modeled on [Irish energy data](https://github.com/PredixDev/minds-machines-europe/tree/master/Electrification%20Challenge/Grid%20Timeseries%20Dataset/LoadForecasting) at the GE Minds+Machines hackathon.

<https://powertechnician.run.aws-usw02-pr.ice.predix.io/demo>

## Installation

Install the Node.js dependencies with:

```
$ npm install
```

Install the Python dependencies with:

```
$ pip install -r requirements.txt
```

You'll also need a running [RabbitMQ](https://www.rabbitmq.com/) instance.

## Development

Point to your RabbitMQ instance with the `MSGFLO_BROKER` environment variable.

To start the local dev server, run:

```
$ npm start
```

If you want to live program the [NoFlo](https://noflojs.org) graph, run:

```
$ npm run dev
```

Then open the URL shown on console.

## Testing

Tests are written in [Mocha](https://mochajs.org/) and located in the `spec/` folder.

Run:

```
$ npm test
```
