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
			
			<v-card
				class="mx-auto"
				max-width="500"
			>
				<v-img
				class="white--text align-end"
				height="300px"
				src="/images/havuz.jpg"
				>
				
				</v-img>

				<v-card-title class="pb-0">GP Combine of Fine Wines "Milestii Mici"</v-card-title>

				<v-card-text class="text--primary">
					<div>
						The Republic of Moldova is not in vain called the "Country where the doors to the wine paradise are open." 
						After all, wine production is the main occupation of the inhabitants of the republic.
						Products of the Quality Wines Combine “Milestii. Mich.” long known, recognized and loved far beyond the borders of Moldova.
						The quality wine factory Milestii Mici is the oldest repository of this “sacred drink”.
					    Any guest is interested in visiting this unique place, the doors of which are open for everyone.
					</div>
				</v-card-text>
				<v-card-actions>
				<v-btn
					color="orange"
					text
				>
					detailed
				</v-btn>
				</v-card-actions>
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