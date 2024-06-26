/**
 * Source: https://learn.codeinstitute.net/courses/course-v1:
 * CodeInstitute+FSD101_WTS+2/courseware/
 * 56a2da0940b4411d8a38c2b093a22c60/24613de4bafc4032882cc1b8799bd4f0/
 * ?child=first
 */

document.addEventListener('DOMContentLoaded', function() {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
    const editButtons = document.getElementsByClassName("btn-edit");

    /**
     * Initializes deletion functionality for the provided delete buttons.
     * 
     * For each button in the `deleteButtons` collection:
     * - Retrieves the associated appointment's ID upon click.
     * - Checks if the appointment ID is valid.
     * - Updates the `deleteConfirm` link's href to point to the 
     *   deletion endpoint for the specific appointment.
     * - Displays a confirmation modal (`deleteModal`) to prompt 
     *   the user for confirmation before deletion.
     * - Logs an error if the appointment ID is not found.
     */
    // Attach event listeners to delete buttons
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let appointmentId = e.target.getAttribute("data-appointment-id");
            if (appointmentId) {
                deleteConfirm.href = `/appointment/appointment_delete/${appointmentId}/`;
                deleteModal.show();
            } else {
                console.error('Appointment ID not found');
            }
        });
    }

    /**
     * Initializes editing functionality for the provided edit buttons.
     * 
     * For each button in the `editButtons` collection:
     * - Retrieves the associated appointment's ID upon click.
     * - Stores the appointment ID for further processing.
     * - Logs an error if the appointment ID is not found.
     */

    // Attach event listeners to edit buttons

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let appointmentId = e.target.getAttribute("data-appointment-id");
            if (appointmentId) {
                /** Redirect browser to a different URL for edititng appointment
            * Source: https://www.geeksforgeeks.org/how-to-redirect-to-another-webpage-using-javascript/
            */
                window.location.href = `/appointment/edit/${appointmentId}/`;
            } 
            else {
                console.error('Appointment ID not found');
            }
        });
    }
});