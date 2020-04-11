<template>
	<div class="content" :style="styles_var" >
		<section
			class="brand"
			v-touch="{
				up: () => swipe('Up'),
				down: () => swipe('Down')
			}"
		>
			<client-only>
				<video-bg
					:sources="['/video/wine_stunning.mp4']"
					img="/images/wine-bottles-cricova-moldova.jpg"
					:bottom_offset="56"
					:reduce_size="isIntersecting"
				>
					<v-row
						align="center"
						justify="center"
					>
						<v-col class="text-center" cols="12">
							<img
								src="/images/mouse-up.png"
								@click="isIntersecting = !isIntersecting"
							>	
						</v-col>	
					</v-row>
				</video-bg>	
			</client-only>	
		</section>
		<section
			v-if="isIntersecting"
			class="articles"
		>
			<!-- v-intersect="onIntersect"
		> -->
			<v-card
				v-for="n in 10" :key="n"
				class="mx-auto elevation-1"
				max-width="344"
			>
				<v-img
					src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
					height="150px"
				></v-img>

				<v-card-title>
				Top western road trips
				</v-card-title>

				<v-card-subtitle>
				1,000 miles of wonder
				</v-card-subtitle>
			</v-card>
		</section>
	</div>
</template>
<script lang="coffee">
import VideoBg from "~/components/video-background"
import ProductCard from "~/components/product-card"
export default {
	name: 'home'
	components: {
		"video-bg": VideoBg
		"product-card": ProductCard
	}
	data: ->
		return {
			allowd_intersection: false
			isIntersecting: false
			offsetTop: 0
			swipeDirection: 'None',
		}
	computed:
		styles_var: ->
			return {
				"--video-cell": if @isIntersecting then "200px" else "calc(100vh - 89px)"
			}
	mounted: ->
		@$nextTick ->
			setTimeout =>
					@allowd_intersection = true
				, 400
	methods:
		swipe: (direction) ->
			if direction is "Up"
				@isIntersecting = true
			else if direction is "Down"
				@isIntersecting = false
			this.swipeDirection = direction

		onIntersect: (entries, observer) ->
			if @allowd_intersection
				@isIntersecting = entries[0].isIntersecting


}
</script>
<style lang="scss" scoped>
.content
{
	display: grid;
	grid-template-rows: var(--video-cell, calc(100vh - 56px)) auto;
	grid-gap: 2em;
	transition: all 0.3s linear;
	section
	{
		&.articles
		{
			padding: 8px;
			display: grid;
			grid-gap: 8px;
			// grid-template-columns: repeat(auto-fill, minmax(45%, 1fr));
		}
	}
}

</style>