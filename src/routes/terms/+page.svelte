<script>
  import { quadInOut } from "svelte/easing";
  import { fly } from "svelte/transition";
  import GuidanceLeft2ShortArrow from "~icons/guidance/left-2-short-arrow";
</script>

<svelte:head>
  <title>Rizz Up | Terms of Service</title>
  <meta name="description" content="Rizz Up Terms of Service" />
</svelte:head>

<div
  class="mx-auto flex flex-col items-start justify-center px-8 py-4 font-serif md:w-3/4 md:px-16 md:py-8 lg:w-1/2"
>
  <h1 in:fly={{ y: 50, duration: 500, easing: quadInOut }}>Terms of Service</h1>

  <p in:fly={{ y: 50, duration: 500, delay: 100, easing: quadInOut }}>
    Welcome to Rizz Up. By using this service, you agree to these terms. Please
    read them carefully.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 200, easing: quadInOut }}>
    1. Acceptance of Terms
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 250, easing: quadInOut }}>
    By accessing or using Rizz Up, you agree to be bound by these Terms of
    Service and all applicable laws and regulations. If you do not agree with
    any part of these terms, you may not use this service.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 300, easing: quadInOut }}>
    2. Use of Service
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 350, easing: quadInOut }}>
    You may use Rizz Up for personal, non-commercial purposes only. You agree
    not to misuse the service or help anyone else do so.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}>
    3. Privacy and Data Protection
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 450, easing: quadInOut }}>
    Your privacy is important. Please refer to the <a
      href="/privacy"
      class="text-blue-500 hover:underline">Privacy Policy</a
    > for information on how I collect, use, and disclose your personal information.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 500, easing: quadInOut }}>
    4. Intellectual Property
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 550, easing: quadInOut }}>
    The content, features, and functionality of Rizz Up are owned by me and are
    protected by international copyright, trademark, patent, trade secret, and
    other intellectual property laws.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 600, easing: quadInOut }}>
    5. Disclaimer of Warranties
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 650, easing: quadInOut }}>
    Rizz Up is provided "as is" without any warranties, expressed or implied. I
    do not guarantee the accuracy of color recommendations or skin tone
    analysis.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 700, easing: quadInOut }}>
    6. Limitation of Liability
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 750, easing: quadInOut }}>
    In no event shall Rizz Up be liable for any indirect, incidental, special,
    consequential or punitive damages, or any loss of profits or revenues.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 800, easing: quadInOut }}>
    7. Changes to Terms
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 850, easing: quadInOut }}>
    I reserve the right to modify these terms at any time. I will always post
    the most current version on this site. By continuing to use Rizz Up after
    changes become effective, you agree to be bound by the revised terms.
  </p>

  <div
    class="flex w-full items-center justify-center py-4 md:py-8"
    in:fly={{ y: 50, duration: 500, delay: 900, easing: quadInOut }}
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
