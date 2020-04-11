import Component from './component.vue'
export default {
	install: (Vue) ->
		name = "i-scroll"
		unless Vue.options.components[name]?
			Vue.component(name, Component)
}