class Doctor {
    constructor(name, specialty, availability) {
      this.name = name;
      this.specialty = specialty;
      this.availability = availability;
    }
  }
  class Patient {
    constructor(name, preferences) {
      this.name = name;
      this.preferences = preferences;
    }
  }
  class Appointment {
    constructor(doctor, patient, time) {
      this.doctor = doctor;
      this.patient = patient;
      this.time = time;
    }
  }
  function scheduleAppointment(doctor, patient, time) {
    if (doctor.availability.includes(time)) {
      let appointment = new Appointment(doctor, patient, time);
      sendReminder(appointment);
      return appointment;
    } else {
      return "Doctor is not available at that time.";
    }
  }
  function sendReminder(appointment) {
    console.log(`Reminder: You have an appointment with Dr. ${appointment.doctor.name} at ${appointment.time}`);
  }
  let doctor1 = new Doctor("Mike", "Pediatrician", ["Monday 9am", "Wednesday 2pm"]);
  let patient1 = new Patient("Alice", "Morning appointments");
  let appointment1 = scheduleAppointment(doctor1, patient1, "Monday 9am");
  console.log(appointment1);
  let appointment2 = scheduleAppointment(doctor1, patient1, "Tuesday 10am");
  console.log(appointment2);
