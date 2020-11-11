document.addEventListener('DOMContentLoaded', () => {
  const monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];
    document.querySelectorAll('.dateSelect').forEach(select => {
        select.onclick = () => {
            console.log(select.textContent);
            var dateValue = parseInt(select.textContent);
            var schedulePopup = document.querySelector(".schedule_confirm");
            var span = document.querySelector(".schedule_confirm_close");
            schedulePopup.style.display = "block";
            var text = document.querySelector("#confirmationText")
            const d = new Date();

            text.textContent = `Please confirm your appointment date of ${monthNames[d.getMonth()]} ${dateValue} at 10AM by clicking submit below!`
            document.querySelector(".dateValue").value = dateValue
            document.querySelector(".monthName").value = monthNames[d.getMonth()]
            span.onclick = () => {
              schedulePopup.style.display = "none";
              alert("Your appointment is not confirmed!")
            }
            window.onclick = function(event) {
              if (event.target == schedulePopup) {
                schedulePopup.style.display = "none";
                alert("Your appointment is not confirmed!")
              }
            }
        }
    });
    document.querySelector('#nextMonth').onclick = () => {
      fetch("next_month")
      .then(console.log('wtf'))
    }
    document.querySelector('#installationComplete').onclick = () => {
      var schedulePopup = document.querySelector('.schedule_confirm');
      var span = document.querySelector('.schedule_confirm_close');
      schedulePopup.style.display = 'block';
      var text = document.querySelector('#confirmationText');
      text.textContent = "Click below to mark this installation as completed."
      span.onclick = () => {
        schedulePopup.style.display = 'none';
        alert('You have not marked this installation as completed!')
      };
      window.onclick = function(event) {
        if (event.target == schedulePopup) {
          schedulePopup.style.display = "none";
          alert('You have not marked this installation as completed!')
        };
      };
    };




});
