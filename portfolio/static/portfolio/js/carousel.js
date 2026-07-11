document.addEventListener('DOMContentLoaded', function () {
  const root = document.getElementById('dashboard-carousel');
  if (!root) return;

  const slides = root.querySelectorAll('.carousel-slide');
  const dots = root.querySelectorAll('.carousel-dot');
  let index = 0;

  function show(i) {
    index = (i + slides.length) % slides.length;
    slides.forEach((slide, n) => {
      slide.classList.toggle('opacity-0', n !== index);
      slide.classList.toggle('pointer-events-none', n !== index);
    });
    dots.forEach((dot, n) => {
      dot.classList.toggle('bg-cyan', n === index);
      dot.classList.toggle('bg-white/25', n !== index);
    });
  }

  root.querySelector('.carousel-prev').addEventListener('click', () => show(index - 1));
  root.querySelector('.carousel-next').addEventListener('click', () => show(index + 1));
  dots.forEach((dot, n) => dot.addEventListener('click', () => show(n)));
});
