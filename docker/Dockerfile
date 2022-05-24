FROM node:17.9-slim

RUN apt-get update && apt-get install -y \
    gnupg \
    libgtk-3.0 \
    libgbm-dev \
    libnss3 \
    libatk-bridge2.0-0 \
    libasound2 \
    wget \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
      --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./ /app

# Install puppeteer so it's available in the container.
RUN npm init -y \
    && npm i -g @vivliostyle/cli@4.11.0