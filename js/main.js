/* D.A.G.R. COMPANY — interações do site */
(function () {
  "use strict";

  document.documentElement.classList.add("js");

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- vídeo de abertura (na home, sempre que se entra no site) ---------- */
  var intro = document.querySelector(".intro");
  if (intro) {
    // não repete quando se volta à Home a partir de outra página do próprio site
    var internal = false;
    try { internal = !!document.referrer && new URL(document.referrer).host === location.host && location.host !== ""; } catch (e) {}
    if (internal) {
      intro.remove();
    } else {
      var video = intro.querySelector("video");
      var bar = intro.querySelector(".intro-bar span");
      document.body.style.overflow = "hidden";

      var closeIntro = function () {
        if (intro.classList.contains("done")) return;
        intro.classList.add("done");
        document.body.style.overflow = "";
        setTimeout(function () { intro.remove(); }, 800);
      };

      // se o vídeo não puder tocar, mostra a animação do escudo em alternativa
      var fallback = function () {
        if (intro.classList.contains("fallback") || intro.classList.contains("done")) return;
        intro.classList.add("fallback");
        setTimeout(closeIntro, 3600);
      };

      // escolhe a versão do vídeo conforme o ecrã e o formato suportado (MP4/H.264, senão WebM/VP9)
      var size = window.innerWidth <= 900 ? "720" : "1080";
      var ext = video.canPlayType('video/mp4; codecs="avc1.640028"') ? "mp4" : "webm";
      video.src = "video/intro-" + size + "." + ext;
      video.addEventListener("timeupdate", function () {
        if (video.duration) bar.style.transform = "scaleX(" + (video.currentTime / video.duration) + ")";
      });
      video.addEventListener("ended", closeIntro);
      video.addEventListener("error", fallback);

      var playing = video.play();
      if (playing && playing.catch) {
        // autoplay bloqueado (ex: modo poupança de energia) -> animação do escudo
        playing.catch(fallback);
      }

      intro.querySelector(".intro-skip").addEventListener("click", closeIntro);
      intro.addEventListener("click", function (e) { if (e.target === video) closeIntro(); });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" || e.key === "Enter" || e.key === " ") closeIntro();
      });
      setTimeout(closeIntro, 12000); // segurança caso o vídeo encrave
    }
  }

  /* ---------- menu móvel ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    var setOpen = function (open) {
      links.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? "✕ CLOSE" : "☰ MENU";
      document.body.style.overflow = open ? "hidden" : "";
    };
    toggle.addEventListener("click", function () {
      setOpen(!links.classList.contains("open"));
    });
    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && links.classList.contains("open")) setOpen(false);
    });
  }

  /* ---------- revelar ao fazer scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- filtro das vagas (recrutamento) ---------- */
  var filterBtns = document.querySelectorAll("[data-filter]");
  var rows = document.querySelectorAll(".positions tbody tr");
  filterBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var f = btn.getAttribute("data-filter");
      filterBtns.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      rows.forEach(function (row) {
        var show = f === "all" ||
          (f === "open" ? row.getAttribute("data-status") === "open" : row.getAttribute("data-team") === f);
        row.hidden = !show;
      });
    });
  });

  /* ---------- copiar link do Discord ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var label = btn.textContent;
      var done = function () {
        btn.textContent = "Copied ✓";
        setTimeout(function () { btn.textContent = label; }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { window.prompt("Copy link:", text); });
      } else {
        window.prompt("Copy link:", text);
      }
    });
  });

  /* ---------- galeria com lightbox ---------- */
  var items = Array.prototype.slice.call(document.querySelectorAll(".gallery button"));
  var lb = document.querySelector(".lightbox");
  if (items.length && lb) {
    var lbImg = lb.querySelector("img");
    var lbCount = lb.querySelector(".lb-count");
    var current = 0;
    var lastFocus = null;

    var show = function (i) {
      current = (i + items.length) % items.length;
      var img = items[current].querySelector("img");
      lbImg.src = items[current].getAttribute("data-full") || img.src;
      lbImg.alt = img.alt;
      lbCount.textContent = (current + 1) + " / " + items.length;
    };
    var open = function (i) {
      lastFocus = document.activeElement;
      show(i);
      lb.classList.add("open");
      document.body.style.overflow = "hidden";
      lb.querySelector(".lb-close").focus();
    };
    var close = function () {
      lb.classList.remove("open");
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    };

    items.forEach(function (btn, i) { btn.addEventListener("click", function () { open(i); }); });
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(current - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(current + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(current - 1);
      if (e.key === "ArrowRight") show(current + 1);
    });

    // deslizar no telemóvel
    var startX = null;
    lb.addEventListener("touchstart", function (e) { startX = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (startX === null) return;
      var dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
      startX = null;
    });
  }

  /* ---------- ano no rodapé ---------- */
  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();

/* ---------- animações extra ---------- */
(function () {
  "use strict";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* entrada escalonada do topo — espera pelo fim da intro na home */
  var staggers = document.querySelectorAll(".stagger");
  var startStagger = function () { staggers.forEach(function (el) { el.classList.add("go"); }); };
  var intro = document.querySelector(".intro");
  if (intro && !reduceMotion) {
    var check = setInterval(function () {
      if (!document.body.contains(intro) || intro.classList.contains("done")) {
        clearInterval(check);
        setTimeout(startStagger, 250);
      }
    }, 100);
  } else {
    startStagger();
  }

  /* atraso em cascata para elementos .reveal lado a lado */
  document.querySelectorAll(".grid, .steps, .req-list").forEach(function (group) {
    var kids = group.querySelectorAll(":scope > .reveal");
    kids.forEach(function (k, i) { k.style.transitionDelay = (i * 0.12) + "s"; });
  });

  /* galeria em cascata */
  var gItems = document.querySelectorAll(".gallery button");
  if (gItems.length) {
    if ("IntersectionObserver" in window && !reduceMotion) {
      var gio = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add("in"); gio.unobserve(e.target); }
        });
      }, { threshold: 0.1 });
      gItems.forEach(function (b, i) { b.style.transitionDelay = ((i % 4) * 0.08) + "s"; gio.observe(b); });
    } else {
      gItems.forEach(function (b) { b.classList.add("in"); });
    }
  }

  /* números a contar (ex: 18+, 2–3, 4) */
  var counters = document.querySelectorAll("[data-count]");
  var runCount = function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    var suffix = el.getAttribute("data-suffix") || "";
    var t0 = null, dur = 1400;
    var step = function (ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if (counters.length) {
    if ("IntersectionObserver" in window && !reduceMotion) {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { runCount(e.target); cio.unobserve(e.target); }
        });
      }, { threshold: 0.6 });
      counters.forEach(function (c) { cio.observe(c); });
    }
  }

  /* barra de progresso + parallax do topo */
  var bar = document.createElement("div");
  bar.className = "scroll-progress";
  document.body.appendChild(bar);
  var heroImg = document.querySelector(".hero-media, .page-hero .bg, .recruit-hero .bg");
  var ticking = false;
  var onScroll = function () {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    var y = window.scrollY;
    bar.style.transform = "scaleX(" + (h > 0 ? y / h : 0) + ")";
    if (heroImg && !reduceMotion && y < window.innerHeight * 1.2) {
      heroImg.style.transform = "translateY(" + (y * 0.3) + "px)";
    }
    ticking = false;
  };
  window.addEventListener("scroll", function () {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();
})();
