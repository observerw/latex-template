FROM ubuntu:22.04

COPY .. /workspace
WORKDIR /workspace

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    perl wget libfontconfig1 git ca-certificates texlive-extra-utils
# for some reason, texlive-extra-utils (for texcount, latexindent, etc.) needs to be installed separately

RUN TINYTEX_INSTALLER=TinyTeX-2 wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh
ENV PATH="${PATH}:/root/bin"

RUN fmtutil-sys --all