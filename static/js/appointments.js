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

    /**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated appointment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific appointment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

    for (let button of deleteButtons) {
        button.addEventListener("click", function(e) {
            const appointmentId = button.getAttribute("data-appointment-id");
            deleteConfirm.href = `/appointment/appointment_delete/${appointmentId}/`;
            deleteModal.show();
        });
    }
});