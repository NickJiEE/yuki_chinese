document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.querySelector('.features-toggle');
    const additionalGrid = document.querySelector('.features-grid.additional');
  
    toggleBtn.addEventListener('click', function() {
      if (additionalGrid.style.display === 'none' || additionalGrid.style.display === '') {
        additionalGrid.style.display = 'flex';
        toggleBtn.textContent = '隐藏'; // Change text to "Hide more"
      } else {
        additionalGrid.style.display = 'none';
        toggleBtn.textContent = '显示更多'; // Change text back to "Show more"
      }
    });
  });