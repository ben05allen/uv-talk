FROM debian:12
ENV DEBIAN_FRONTEND=noninteractive

# copy in uv binary
# Note: there is currently no Python installed
# but doesn't currently work for musl-based distros, such as Alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# update container
RUN apt-get update \
    && apt-get dist-upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# switch to non-root user
RUN groupadd -r appuser \ 
    && useradd -r -g appuser appuser \
    && mkdir /home/appuser \
    && chown -R appuser:appuser /home/appuser
WORKDIR /home/appuser
USER appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"

# install python and project requirements
COPY --chown=appuser:appuser ./pyproject.toml .
RUN uv sync
COPY --chown=appuser:appuser src .

# run
CMD [ "uv", "run", "main.py" ]