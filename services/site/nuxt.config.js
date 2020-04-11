const colors = require('vuetify/es5/util/colors').default
module.exports = {
	mode: 'universal',
	/*
	** Headers of the page
	*/
	head: {
		title: process.env.npm_package_name || '',
		meta: [
		{ charset: 'utf-8' },
		{ name: 'viewport', content: 'width=device-width, initial-scale=1' },
		{ hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
		],
		link: [
		{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
		{ rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons|Hind+Madurai:300,400,500,700' }
		]
	},
	/*
	** Customize the progress-bar color
	*/
	loading: { color: '#fff' },
	/*
	** Global CSS
	*/
	css: [
	],
	/*
	** Plugins to load before mounting the App
	*/
	plugins: [
		{ src: '~/plugins/scroll/index.coffee', ssr: false }
	],
	/*
	** Nuxt.js dev-modules
	*/
	devModules: [
		'@nuxtjs/vuetify',
		],
	/*
	** Nuxt.js modules
	*/
	modules: [
		'@nuxtjs/axios',
  		'@nuxtjs/auth',
		'@nuxtjs/svg'
	],
	/*
		** vuetify module configuration
		** https://github.com/nuxt-community/vuetify-module
		*/
		vuetify: {
			customVariables: ['~/assets/scss/variables.scss'],
			defaultAssets: {
				font: false,
			},
			theme: {
				dark: false,
				icons: {
					iconfont: 'mdi',
				},
				themes: {
					dark: {
						primary: "#D82A2B",
						accent: colors.grey.darken3,
						secondary: colors.amber.darken3,
						info: colors.teal.lighten1,
						warning: colors.amber.base,
						error: colors.deepOrange.accent4,
						success: colors.green.accent3
					},
					light: {
						primary: "#D82A2B",
						accent: colors.grey.darken3,
						secondary: colors.amber.darken3,
						info: colors.teal.lighten1,
						warning: colors.amber.base,
						error: colors.deepOrange.accent4,
						success: colors.green.accent3
					}
				}
			}
		},




	// See https://github.com/nuxt-community/axios-module#options

	axios: {
		baseURL: process.env.SERVER_DOMAIN_NAME,
		browserBaseURL: process.env.BROWSER_DOMAIN_NAME,
		// xsrfHeaderName: 'X-CSRFToken',
		// xsrfCookieName: 'csrftoken',
		headers: { 'Content-Type': 'application/json' },
		

	}, 
	/*
	** Build configuration
	*/
	build: {
			/*
			** You can extend webpack config here
			*/
			extend (config, ctx) {
			config.module.rules.push(
				{
					test: /\.coffee$/,
					use: 'coffee-loader',
					exclude: /(node_modules)/
				}
			)
		}
	}
}
