console.log("JS loaded");



const templates = [
    {
      id: 1,
      title: 'Daily Self Tracking',
      category: 'Self-tracking',
      description: 'Time follows who you are!',
      image: 'https://media.licdn.com/dms/image/v2/D4D12AQHVHLQKAFS3Mg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1676275664910?e=1748476800&v=beta&t=6Ivx3VpBbq7gPNDvIs8oPmHkOYJVx0bHURcGOIQsCkc',
      link:'https://docs.google.com/spreadsheets/d/1Bdy0y30Kpsaqk6Thu8lZ5wmBvASGaSOe6NnKykbJA9k/edit?usp=sharing',
      button:'View Tracker'
    },
    {
      id: 2,
      title: 'Insightful Questions',
      category: 'Enquiry',
      description: 'Diagnosis is Cure!',
      image: "/static/images/inquire.jpg",
      link:'https://docs.google.com/document/d/1FPimBYyJ-IQFy4-KNSCZd2zfsnGo7DOEaD5jzYoEWrg/edit?tab=t.0',
      button:'Know your disease'
    },
    {
      id: 3,
      title: 'Personalized one-to-one counselling',
      category: 'Counselling',
      description: 'Safe, secured & privacy ensured!',
      image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmrcInFMVLf9XTNlx0ExHsYnKIWRbktSGNOdIA-mDTmDZ6V3Jk-fnGYUd0pS_BUmouV9Y&usqp=CAU',
      link:'https://docs.google.com/forms/d/e/1FAIpQLSfjv6c7LwgkVjz3Pf--68mX-uTCrYPXs0-V2JBrgqm9OOgxIA/viewform?usp=header',
      button: 'Book now'
    },
    {
      id: 4,
      title: 'Fun Quiz',
      category: 'Assessment',
      description: 'Real laughter comes after knowing the self!',
      image: 'https://img.freepik.com/premium-photo/illuminating-image-depicting-human-brain-inside-light-bulb_884296-108047.jpg',
      link:'https://docs.google.com/forms/d/e/1FAIpQLSf06RME89oaBdAN0rqjeQd24q9SmqhERXwOO0bah35cuPvEzw/viewform?usp=header',
      button: 'Play now'
    },
    {
      id: 5,
      title: 'Understand the Core Concepts',
      category: 'Foundation',
      description: 'Videos with self-evalution',
      image: 'https://lxd.org/wp-content/uploads/2023/11/what-is-lxd-focus.png',
      link:djangoUrls.allVideos,
      button: 'Explore Now'
    },
    {
      id: 6,
      title: 'Know your Mother\'s Health',
      category: 'Climate Change',
      description: 'Mother is no other!',
      image: 'https://delhigreens.com/wp-content/uploads/2010/05/mother-nature-on-mothers-day.jpg',
      link:'',
      button: 'Check Now'
    },
    {
      id: 7,
      title: '',
      category: 'Assessment',
      description: '',
      image: '',
      link:'',
      button: 'Play now'
    },
    {
      id: 8,
      title: '',
      category: 'Assessment',
      description: '',
      image: '',
      link:'',
      button: 'Play now'
    },
    
  ];

  // Define CSS classes in a separate variable
const cardClasses = [
  "p-[20px]","rounded-[8px]",
  "[box-shadow:0_0_10px_rgba(02,_0,_0,_0.1)]",
  "hover:shadow-[-1px_3px_46px_-10px_#aaaaff]",
  "hover:[transition:1.0s]",
  "bg-[rgb(30,32,33)]", 
];

function loadTemplates() {
  const container = document.getElementById('template-container');
  container.innerHTML = '';
  
  templates.forEach((template) => {
    const card = document.createElement('div');
    // card.classList.add("card p-[20px] rounded-[8px] hover:[box-shadow:0_0_30px_rgba(41,_31,_20,_0.9)] hover:[transition:0.5s] w-full h-[150px] object-contain rounded-[5px]");
    // Add classes to the card element
    cardClasses.forEach((className) => {
      card.classList.add(className);
    });

        card.innerHTML = `
            <div class="flex flex-col items-center text-center p-4">
  <img class="w-full h-40 object-contain rounded-md mb-2" src="${template.image}" alt="${template.title}">

  <h2 class="text-xl font-semibold mt-2 mb-1">${template.title}</h2>
  
  <p class="text-gray-400 mb-2">${template.description}</p>
  
  <button onclick="window.open('${template.link}', '_blank')" 
          class="px-4 py-2 bg-blue-500 text-white rounded-md cursor-pointer hover:bg-blue-700">
      ${template.button}
  </button>
</div>        
`;

        container.appendChild(card);
    });
}


//Searching
  // function filterTemplates() {
  //   const searchValue = document
  //     .getElementById('search')
  //     .value.toLowerCase();
  //   const filteredTemplates = templates.filter((template) =>
  //     template.title.toLowerCase().includes(searchValue)
  //   );
  //   const container = document.getElementById('template-container');
  //   container.innerHTML = '';
  //   filteredTemplates.forEach((template) => {
  //     const card = document.createElement('div');
  //     card.classList.add('card');
  //     card.innerHTML = `
  //               <img src="${template.image}" alt="${template.title}">
  //               <h2>${template.title}</h2>
  //               <p>${template.description}</p>
  //               <button>Download</button>
  //           `;
  //     container.appendChild(card);
  //   });
  // }

  window.onload = loadTemplates;
