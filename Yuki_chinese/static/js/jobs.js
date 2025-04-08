// document.querySelector('.large-hero').style.backgroundImage = `url(/static/images/job.jpg)`;
const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modal-title");
const modalImg = document.getElementById("modal-img");
const modalText = document.getElementById("modal-text");

const modalData = {
  1: {
    title: "在线申请",
    img: "/static/images/step1.avif",
    text: "请通过我们的网站联系微信客服 (Yukichulian) 并填写相关信息。"
  },
  2: {
    title: "初步筛选",
    img: "/static/images/step2.avif",
    text: "HR将评估您所提供的信息是否符合职位要求。"
  },
  3: {
    title: "线上面试",
    img: "/static/images/step3.avif",
    text: "与HR进行30分钟的线上视频面试并回答工作相关问题。"
  },
  4: {
    title: "录用通知",
    img: "/static/images/step5.avif",
    text: "通过以上环节后，我们将在面试结束后24小时内正式发出录用通知。"
  }
};

function openModal(step) {
  modal.style.display = "flex";
  modalTitle.textContent = modalData[step].title;
  modalImg.src = modalData[step].img;
  modalText.textContent = modalData[step].text;
}

function closeModal() {
  modal.style.display = "none";
}

function toggleFAQ(element) {
    const item = element.closest('.faq-item');
    const toggle = element.querySelector('.faq-toggle');
  
    item.classList.toggle('open');
  
    // Update the toggle sign
    if (item.classList.contains('open')) {
      toggle.textContent = '−';
    } else {
      toggle.textContent = '+';
    }
  }
  