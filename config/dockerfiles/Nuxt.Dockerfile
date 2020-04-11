FROM node:13.11.0-alpine AS base-dependencies

ENV APP_ROOT /app
ENV SASS_BINARY_SITE=https://npm.taobao.org/mirrors/node-sass/

RUN mkdir ${APP_ROOT}

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories && \
	echo "**** install build packages ****" && \
    apk add --no-cache make gcc g++ python curl git libc6-compat && \
    cd /tmp && \
    curl -#L https://github.com/tj/node-prune/releases/download/v1.0.1/node-prune_1.0.1_linux_amd64.tar.gz | tar -xvzf- && \
    mv -v node-prune /usr/local/bin && rm -rvf * && \
    echo "yarn cache clean && node-prune" > /usr/local/bin/node-clean && chmod +x /usr/local/bin/node-clean && \
    npm config set registry https://registry.npm.taobao.org/ && \
    npm install --global cross-env
WORKDIR ${APP_ROOT}


FROM base-dependencies AS development-env
ENV HOST 0.0.0.0
ENV NODE_ENV=development
COPY /services/site/package.json ${APP_ROOT}
COPY /services/site/package-lock.json ${APP_ROOT}
RUN npm install && node-clean


FROM development-env AS build-env
COPY /services/site/ /app
RUN npm run build


FROM base-dependencies AS prep-production-env
COPY --from=development-env /app/package.json /app
COPY --from=development-env /app/package-lock.json /app
RUN npm install --production && \
	node-clean



FROM node:13.11.0-alpine AS production-env
ENV NODE_ENV=production
ENV HOST 0.0.0.0

RUN mkdir /app
WORKDIR /app

ADD /services/site/package.json /app
ADD /services/site/nuxt.config.js /app

COPY --from=build-env /services/server /app/server/
COPY --from=prep-production-env /services/node_modules /app/node_modules/
COPY --from=build-env /services/.nuxt /app/.nuxt/
COPY --from=build-env /services/static /app/static/

EXPOSE 3000

CMD ["node", "server/index.js"]


