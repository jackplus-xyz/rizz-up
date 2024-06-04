<script>
	import GuidanceLeft2ShortArrow from '~icons/guidance/left-2-short-arrow';
	const features = [
		'🤳 Skin tone analysis using computer vision algorithms',
		'🎨 Personalized color palette generation based on skin tones',
		'📷 User-uploaded photo support',
		'📱 Social media sharing integration',
		'👚 Image-generation tools for virtual dressing',
		'🛍️ Shopping links for easy access to recommended colors'
	];
</script>

<svelte:head>
	<title>Rizz Up | About</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div
	class="mx-auto flex flex-col items-start justify-center px-8 py-4 font-serif md:w-3/4 md:px-16 md:py-8 lg:w-1/2"
>
	<h1>About</h1>
	<p>
		<strong>Rizz Up</strong>
		is a web application that analyzes user skin tones and generates personalized color palettes. The
		app will accept a user-uploaded photo, analyze the skin tone and provide a list of colors that complement
		the user the most. Users can share their results on social media. They can also use image-generation
		tools to virtually dress in their recommended color palette, providing shopping links for easy access
		to those colors in real life.
	</p>

	<h2>Features</h2>
	<ol>
		{#each features as feature}
			<li>
				{feature}
			</li>
		{/each}
	</ol>

	<h2>How Does it Work?</h2>
	<p>
		Color theory is a complex science that involves understanding how colors interact with each
		other. What
		<strong class="italic">Rizz Up</strong>
		does is it will try to find the color that looks the best on you based on your skin tone. It may
		be affected by the lighting in the photo, but it will give you a good idea of what colors look good
		on you. Then you can use this information as a guide when shopping for new clothes.
	</p>
	<h3>Sounds Good, but...</h3>
	<h4>What will you do with my photo?</h4>
	<p>
		<strong class="italic">Rizz Up</strong>
		is an open-source project aims to help people find the best color for their skin tone. The app will
		not store any of user's photo or personal information. If you are concerned about privacy, you can
		also select a default skin tone that is the closest to yours and see the color palette generated
		for that skin tone.
	</p>
	<h4>Who are you and why should I trust you?</h4>
	<p>
		Glad you asked! My name is <a
			href="https://jackplus.xyz/"
			class="font-bold underline-offset-4 transition-all duration-100 ease-out hover:underline"
			>Jack Huang</a
		>. Like you may find on 90% of other cover letters, I'm also a software engineer who's
		passionate about building tools. You can find more of them
		<a href="https://jackplus.xyz/projects" class="font-bold underline-offset-4 hover:underline"
			>here</a
		>. This project was inspired by a reels on Instagram where I find you can get advices from
		professional stylists in Korea, who will recommend clothes based on your skin tone. I thought it
		would be cool to build a tool that can do that for everyone. And I'm also very concerned about
		my privacy, so I made sure that this app doesn't store any of your personal information.
	</p>
	<h4>How is it done?</h4>
	<p>
		The app will use Python libraries to analyze your skin tones and generate a color palette, which
		you can then:
	</p>
	<ol class="ml-6 list-disc md:ml-4">
		<li>Save the color palette for future reference</li>
		<li>Share the results and see what you friends think</li>
		<li>Explore the shopping links that matches the color</li>
		<li>Try on the virtual clothes with image-generation tools</li>
	</ol>

	<div class="flex w-full items-center justify-center py-4 md:py-8">
		<h2>
			<a href="/" class="group relative flex">
				Cool, right? Let's get started!
				<span class="ml-2 transition-all group-hover:translate-x-2 md:ml-4">
					<GuidanceLeft2ShortArrow />
				</span>
			</a>
		</h2>
	</div>
</div>
