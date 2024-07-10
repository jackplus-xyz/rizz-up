<script>
  import { quadInOut } from "svelte/easing";
  import { fly } from "svelte/transition";
  import GuidanceLeft2ShortArrow from "~icons/guidance/left-2-short-arrow";
  const features = [
    "🤳 Skin tone analysis using computer vision algorithms",
    "🎨 Personalized color palette generation based on skin tones",
    "📷 User-uploaded photo support",
    // "📱 Social media sharing integration",
    // "👚 Image-generation tools for virtual dressing",
    // "🛍️ Shopping links for easy access to recommended colors",
  ];
</script>

<svelte:head>
  <title>Rizz Up | About</title>
  <meta name="description" content="About this app" />
</svelte:head>

<div
  class="mx-auto flex flex-col items-start justify-center px-8 py-4 font-serif md:w-3/4 md:px-16 md:py-8 lg:w-1/2"
>
  <h1 in:fly={{ y: 50, duration: 500, easing: quadInOut }}>About</h1>
  <p in:fly={{ y: 50, duration: 500, delay: 100, easing: quadInOut }}>
    <span class="font-bold italic">Rizz Up</span>
    is a web application that analyzes user skin tones and generates personalized
    color palettes. The app will accept a user-uploaded photo, analyze the skin tone
    and provide a list of colors that complement the user the most.
    <!-- Users can share -->
    <!-- their results on social media. They can also use image-generation tools to virtually -->
    <!-- dress in their recommended color palette, providing shopping links for easy access -->
    <!-- to those colors in real life. -->
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 200, easing: quadInOut }}>
    Features
  </h2>
  <ol in:fly={{ y: 50, duration: 500, delay: 250, easing: quadInOut }}>
    {#each features as feature}
      <li>
        {feature}
      </li>
    {/each}
  </ol>

  <h2 in:fly={{ y: 50, duration: 500, delay: 300, easing: quadInOut }}>
    How Does it Work?
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 350, easing: quadInOut }}>
    Color theory is a complex science that involves understanding how colors
    interact with each other. What
    <strong class="italic">Rizz Up</strong>
    does is it will try to find the color that looks the best on you based on your
    skin tone. It may be affected by the lighting in the photo, but it will give
    you a good idea of what colors look good on you. Then you can use this information
    as a guide when shopping for new clothes.
  </p>
  <h3 in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}>
    Sounds Good, but...
  </h3>
  <h4 in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}>
    What will you do with my photo?
  </h4>
  <p in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}>
    <strong class="italic">Rizz Up</strong>
    is an project aims to help people find the best color for their skin tone. The
    app will <span class="font-bold italic text-destructive">NOT</span> store any
    of user's photo or personal information.
  </p>
  <h4 in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}>
    Who are you and why should I trust you?
  </h4>
  <p in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}>
    Glad you asked! My name is <a
      href="https://jackplus.xyz/"
      class="font-bold transition-all duration-100 ease-out hover:underline"
      >Jack Huang</a
    >. I'm a software engineer who's passionate about building tools. You can
    find more of them
    <a href="https://jackplus.xyz/projects" class="font-bold hover:underline"
      >here</a
    >. This project was inspired by a reels on Instagram where I find you can
    get advices from professional stylists in Korea, who will recommend clothes
    based on your skin tone. I thought it would be cool to build a tool that can
    do that for everyone. Privacy is a big cocern for me, so I made sure that
    this app doesn't store any of your personal information. The image data will
    be stored in your browser's local storage for the duration of your visit. It
    won't be stored in any database. (So I don't have to pay for it! 😂)
  </p>
  <h4 in:fly={{ y: 50, duration: 500, delay: 450, easing: quadInOut }}>
    How is it done?
  </h4>
  <p in:fly={{ y: 50, duration: 500, delay: 450, easing: quadInOut }}>
    The app uses
    <a
      href="https://pypi.org/project/retina-face/"
      class="font-bold hover:underline"
      >a deep learning based cutting-edge facial detector for Python</a
    >
    to determine the facial area, then send it to
    <a href="https://claude.ai/" class="font-bold hover:underline">Claude</a>,
    for skin tone analysis. The result is then used to generate a color palette,
    which you can then:
  </p>
  <ol
    class="ml-6 list-disc md:ml-4"
    in:fly={{ y: 50, duration: 500, delay: 500, easing: quadInOut }}
  >
    <li>Save the recommended color palette for future reference</li>
    <li>Avoid buying clothes that don't match your skin tone</li>
    <li>Share the results and see what you friends think</li>
    <!-- <li>Explore the shopping links that matches the color</li> -->
    <!-- <li>Try on the virtual clothes with image-generation tools</li> -->
  </ol>

  <div
    class="flex w-full items-center justify-center py-4 md:py-8"
    in:fly={{ y: 50, duration: 500, delay: 600, easing: quadInOut }}
  >
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
