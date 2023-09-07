# process

Charalampos Kontogiannis


APP:
Η εφαρμογή δέχεται ένα .jpeg αρχείο και επιλέγουμε εμείς αν και πόσο θα αλλάξουμε την φωτεινότητα και την ευκρίνεια αυτού.
Αρχικά ωστόσο, αυτή η επεξεργασία γινόταν με ένα δοθέν βίντεο. Αλλά για διάφορους λόγους έγινε η μετατροπή στην εκδοχή με το αρχείο εικόνας.
Η εφαρμογή βρέθηκε κατόπιν αναζήτησης στο google, σε αυτό το url https://pyshine.com/How-to-quickly-deploy-flask-application-for-video/.
#TESTs
#App execution


GIT:
Έχει δημιουργηθεί ένα repo στο GitHub https://github.com/kontoharis/process.
Είναι συγχρονισμένο τοπικά για να γίνονται commits και pushes οι αλλαγές που χρειάζονταν κατά την ανάπτυξη.
Τα pipelines υλοποιήθηκαν με yaml σε GitHub actions.


Docker:
Οι εντολές που δημιουργούν το container με το app μας.
docker build -t flask-app .    #δημιουργία docker image βάσει του dockerfile
docker run -p 80:80 flask-app    #εκτέλεση docker image -> δημιουργία container


AWS public deployment:
Δημιουργήθηκε ένα EC2 instance με ένα χρήστη, τους απαραίτητους ρόλους και ένα ECR repo στο οποίο γίνεται build το image.
Το web-app απαντάει σε αυτή την public IP του instance: http://13.51.204.248/
