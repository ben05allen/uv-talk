# Running code with `uv`

A simple Docker environment example using `uv`.

Of course, Docker is not required, but 🐄 remember to add the Cowsay dependency 🐄, which has intentionally been missed;

```[bash]
uv add cowsay
```

To run locally;

```[bash]
uv run src/main.py
```

## Create the Image

```[bash]
just b
```

## Run the Container

```[bash]
just r
```
