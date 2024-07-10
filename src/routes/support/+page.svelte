<script>
  import { quadInOut } from "svelte/easing";
  import { fly } from "svelte/transition";
  import GuidanceLeft2ShortArrow from "~icons/guidance/left-2-short-arrow";

  const faqs = [
    {
      question: "How accurate is the skin tone analysis?",
      answer:
        "The skin tone analysis uses Claude, a AI model with a knowledge of 12 seasons color analysis to determine your skin tone, and suggest colors that complement it. However, the quality of the input photo and lighting conditions can affect the accuracy. For best results, use a well-lit photo with a neutral background.",
    },
    {
      question: "Is my photo stored on your servers?",
      answer:
        "No, I do not store your photos on any servers. The image is sent to a Flask app for face detection, then sent to Claude for color analysis. The result and the photo data is only stored temporarily in your browser's local storage during your session.",
    },
    {
      question: "How do I interpret the color palette results?",
      answer:
        "The color palette generated for you includes colors that complement your skin tone. These colors are generally flattering for clothing, accessories, and makeup. You can use this palette as a guide when shopping or choosing outfits.",
    },
  ];
</script>

<svelte:head>
  <title>Rizz Up | Support</title>
  <meta name="description" content="Rizz Up Support and FAQs" />
</svelte:head>

<div
  class="mx-auto flex flex-col items-start justify-center px-8 py-4 font-serif md:w-3/4 md:px-16 md:py-8 lg:w-1/2"
>
  <h1 in:fly={{ y: 50, duration: 500, easing: quadInOut }}>Support</h1>

  <p in:fly={{ y: 50, duration: 500, delay: 100, easing: quadInOut }}>
    Welcome to the Rizz Up support page. Here you'll find answers to frequently
    asked questions and helpful information about using the app.
  </p>

  <h3 in:fly={{ y: 50, duration: 500, delay: 200, easing: quadInOut }}>
    Frequently Asked Questions
  </h3>

  <div in:fly={{ y: 50, duration: 500, delay: 300, easing: quadInOut }}>
    {#each faqs as faq}
      <div class="mb-4">
        <h4>
          {faq.question}
        </h4>

        <p>{faq.answer}</p>
      </div>
    {/each}
  </div>

  <h2 in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}>
    Still Need Help?
  </h2>

  <p in:fly={{ y: 50, duration: 500, delay: 450, easing: quadInOut }}>
    If you couldn't find the answer you were looking for, please don't hesitate
    to reach out to me. You can contact me through the <a
      href="/contact"
      class="text-blue-500 hover:underline">contact page</a
    >.
  </p>

  <div
    class="flex w-full items-center justify-center py-4 md:py-8"
    in:fly={{ y: 50, duration: 500, delay: 500, easing: quadInOut }}
  >
    <h2>
      <a href="/" class="group relative flex">
        Back to Home
        <span class="ml-2 transition-all group-hover:translate-x-2 md:ml-4">
          <GuidanceLeft2ShortArrow />
        </span>
      </a>
    </h2>
  </div>
</div>
