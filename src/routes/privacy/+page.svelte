<script>
  import { quadInOut } from "svelte/easing";
  import { fly } from "svelte/transition";
  import GuidanceLeft2ShortArrow from "~icons/guidance/left-2-short-arrow";
</script>

<svelte:head>
  <title>Rizz Up | Privacy Policy</title>
  <meta name="description" content="Rizz Up Privacy Policy" />
</svelte:head>

<div
  class="mx-auto flex flex-col items-start justify-center px-8 py-4 font-serif md:w-3/4 md:px-16 md:py-8 lg:w-1/2"
>
  <h1 in:fly={{ y: 50, duration: 500, easing: quadInOut }}>Privacy Policy</h1>

  <p in:fly={{ y: 50, duration: 500, delay: 100, easing: quadInOut }}>
    At Rizz Up, I am committed to protecting your privacy. This Privacy Policy
    explains how I collect, use, and safeguard your information when you use
    this service.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 200, easing: quadInOut }}>
    1. Information I Collect
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 250, easing: quadInOut }}>
    I collect minimal personal information necessary to provide the service.
    This includes:
  </p>
  <ul
    class="ml-6 list-disc"
    in:fly={{ y: 50, duration: 500, delay: 250, easing: quadInOut }}
  >
    <li>
      Photos you upload for skin tone analysis (temporarily stored in your
      browser's local storage)
    </li>
  </ul>

  <h2 in:fly={{ y: 50, duration: 500, delay: 300, easing: quadInOut }}>
    2. How I Use Your Information
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 350, easing: quadInOut }}>
    I use the information I receive to:
  </p>
  <ul class="ml-6 list-disc">
    <li>
      Provide and improve the skin tone analysis and color recommendation
      service
    </li>
    <li>Analyze usage patterns to enhance user experience</li>
    <li>Respond to your inquiries and support requests</li>
  </ul>

  <h2 in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}>
    3. Data Security
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 450, easing: quadInOut }}>
    I implement reasonable security measures to protect your personal
    information. However, no method of transmission over the Internet or
    electronic storage is 100% secure, and I cannot guarantee absolute security.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 500, easing: quadInOut }}>
    4. Third-Party Services
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 550, easing: quadInOut }}>
    Rizz Up may use third-party services that collect, monitor and analyze this
    type of information in order to increase the service's functionality. These
    third-party service providers have their own privacy policies addressing how
    they use such information.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 600, easing: quadInOut }}>
    5. Your Data Rights
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 650, easing: quadInOut }}>
    You have the right to access, correct, or delete your personal information.
    If you wish to exercise these rights, please contact me using the
    information provided in the Contact section.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 700, easing: quadInOut }}>
    6. Changes to This Privacy Policy
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 750, easing: quadInOut }}>
    I may update this Privacy Policy from time to time. I will notify you of any
    changes by posting the new Privacy Policy on this page. You are advised to
    review this Privacy Policy periodically for any changes.
  </p>

  <h2 in:fly={{ y: 50, duration: 500, delay: 800, easing: quadInOut }}>
    7. Contact Me
  </h2>
  <p in:fly={{ y: 50, duration: 500, delay: 850, easing: quadInOut }}>
    If you have any questions about this Privacy Policy, please contact me with
    through the <a href="/contact" class="text-blue-500 hover:underline"
      >contact page</a
    >.
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

