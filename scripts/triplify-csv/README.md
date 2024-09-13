## Small Script Project for Triplifying CSV Files

### Config Format

The idea of the config is to try and slightly grow out of a specific solution. It will be formatted as follows:

```json
{
  "object_1": {
    "predicate": "ext:id",
    "data-type": "string"
  },
  "object_2": {
    "predicate": "ext:hasLocation",
    "type": "prov:Location",
    "class": {
      "predicate": "rdfs:prefLabel",
      "data-type": "string"
    }
  }
}
```

In the example above, we have definitions for how an erfgoed is connected to its objects. What it translates to:

```ttl
<http://erfgoed_1>
  <ext:id> "ABC" ;
  ext:hasLocation <http://location_1> .

<http://location_1>
  a prov:Location ;
  rdfs:label "Gent" .
```

### Build the image

Run this command inside `scripts/triplify-csv`.

```sh
docker build --no-cache -t triplify-csv .
```

### Run the container

Run this command inside `scripts/triplify-csv`.

```sh
docker run -it --rm triplify-csv:latest
```