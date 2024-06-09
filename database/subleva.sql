DROP DATABASE IF EXISTS subleva;
CREATE DATABASE IF NOT EXISTS subleva;

USE subleva;

CREATE TABLE IF NOT EXISTS users
(
    name     VARCHAR(255) NOT NULL,
    dob      DATETIME,
    userName VARCHAR(255),
    id       INT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS countries
(
    name     VARCHAR(255) UNIQUE  NOT NULL,
    location DECIMAL(7, 5) UNIQUE NOT NULL,
    id       INT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS countryStats (
    countryID INT,
    year INT,
    numApplications INT,
    numRejected INT,
    numGranted INT,
    numOther INT,
    numClosed INT,
    population INT,
    PRIMARY KEY (year, countryID),
    FOREIGN KEY (countryID) REFERENCES countries(id)
);

CREATE TABLE IF NOT EXISTS volunteers
(
    name VARCHAR(255) NOT NULL,
    id  INT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS appointments
(
    volunteerID   INT NOT NULL,
    appDate          DATE,
    appointmentID INT AUTO_INCREMENT,
    subject VARCHAR(30),
    weekday VARCHAR(11),
    PRIMARY KEY (appointmentID),
    foreign key (volunteerID) REFERENCES volunteers (id)
);

SELECT * from appointments;

CREATE TABLE IF NOT EXISTS posts
(
    postID      INT AUTO_INCREMENT,
    postContent VARCHAR(1500),
    createdAt   DATETIME,
    displayName VARCHAR(70),
    migrantID   INT NOT NULL,
    PRIMARY KEY (postID),
    FOREIGN KEY (migrantID) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS communityEvent
(
    eventDate          DATE,
    eventID       INT AUTO_INCREMENT,
    name          VARCHAR(255),
    duration      INT,
    venueCapacity INT,
    PRIMARY KEY (eventID)
);

CREATE TABLE IF NOT EXISTS appointmentAttendees
(
    attendeeID INT,
    appointmentID    INT AUTO_INCREMENT,
    primary key (attendeeID, appointmentID),
    FOREIGN KEY (attendeeID) REFERENCES users(id),
    FOREIGN KEY (appointmentID) REFERENCES appointments(appointmentID)
);

CREATE TABLE IF NOT EXISTS refugeeCohort(
    cohortID INT,
    year INT,
    asylumCountryID INT,
    originCountryID INT,
    PRIMARY KEY  (cohortID),
    FOREIGN KEY (asylumCountryID) REFERENCES countries(id),
    FOREIGN KEY (originCountryID) REFERENCES countries(id)
);

INSERT INTO users (id, name, userName, dob) VALUES ('1', 'Kristina', 'Reading', '1988-02-22');
INSERT INTO users (id, name, userName, dob) VALUES ('2', 'Aura', 'Pilsworth', '1971-06-03');
INSERT INTO users (id, name, userName, dob) VALUES ('3', 'Louella', 'Campion', '1965-02-19');
INSERT INTO users (id, name, userName, dob) VALUES ('4', 'Guilbert', 'Hirthe', '1964-04-26');
INSERT INTO users (id, name, userName, dob) VALUES ('5', 'Johannes', 'Sainsbury-Brown', '1968-07-21');
INSERT INTO users (id, name, userName, dob) VALUES ('6', 'Valerie', 'Trewhitt', '1955-04-06');
INSERT INTO users (id, name, userName, dob) VALUES ('7', 'Mar', 'Baalham', '2002-05-14');
INSERT INTO users (id, name, userName, dob) VALUES ('8', 'Aviva', 'Scimone', '1999-09-20');
INSERT INTO users (id, name, userName, dob) VALUES ('9', 'Johna', 'Chainey', '1989-03-02');
INSERT INTO users (id, name, userName, dob) VALUES ('10', 'Edie', 'Denerley', '1957-10-30');
INSERT INTO users (id, name, userName, dob) VALUES ('11', 'Jelene', 'Gages', '1937-12-25');
INSERT INTO users (id, name, userName, dob) VALUES ('12', 'Nikki', 'Heninghem', '1962-08-11');
INSERT INTO users (id, name, userName, dob) VALUES ('13', 'Davina', 'Goscar', '1988-10-23');
INSERT INTO users (id, name, userName, dob) VALUES ('14', 'Dulcinea', 'Polglase', '1963-03-08');
INSERT INTO users (id, name, userName, dob) VALUES ('15', 'Fredi', 'Tavner', '1951-06-09');
INSERT INTO users (id, name, userName, dob) VALUES ('16', 'Darrin', 'Gethouse', '1996-01-21');
INSERT INTO users (id, name, userName, dob) VALUES ('17', 'Ester', 'Durning', '1956-08-10');
INSERT INTO users (id, name, userName, dob) VALUES ('18', 'Launce', 'Salery', '1945-08-13');
INSERT INTO users (id, name, userName, dob) VALUES ('19', 'Riley', 'Warrick', '1989-09-20');
INSERT INTO users (id, name, userName, dob) VALUES ('20', 'Halli', 'Geraudel', '1943-05-30');
INSERT INTO users (id, name, userName, dob) VALUES ('21', 'Deloria', 'Abelson', '2004-10-09');
INSERT INTO users (id, name, userName, dob) VALUES ('22', 'Claudina', 'Hufton', '1979-11-15');
INSERT INTO users (id, name, userName, dob) VALUES ('23', 'Abigael', 'Atwell', '1993-10-24');
INSERT INTO users (id, name, userName, dob) VALUES ('24', 'Arabela', 'O''Luby', '1972-04-28');
INSERT INTO users (id, name, userName, dob) VALUES ('25', 'Ellerey', 'Courcey', '1950-01-26');
INSERT INTO users (id, name, userName, dob) VALUES ('26', 'Sanderson', 'Brissenden', '1993-08-05');
INSERT INTO users (id, name, userName, dob) VALUES ('27', 'Sergio', 'Wilcher', '1979-10-06');
INSERT INTO users (id, name, userName, dob) VALUES ('28', 'Hetty', 'Sivil', '1962-10-09');
INSERT INTO users (id, name, userName, dob) VALUES ('29', 'Lief', 'Ivanikhin', '1960-04-14');
INSERT INTO users (id, name, userName, dob) VALUES ('30', 'Wayland', 'Skowcraft', '1988-03-01');
INSERT INTO users (id, name, userName, dob) VALUES ('31', 'Rhodia', 'Cudby', '1954-01-10');
INSERT INTO users (id, name, userName, dob) VALUES ('32', 'Lorene', 'Cecchetelli', '1996-01-17');
INSERT INTO users (id, name, userName, dob) VALUES ('33', 'Bambie', 'Goldbourn', '2000-07-12');
INSERT INTO users (id, name, userName, dob) VALUES ('34', 'Gay', 'Karolewski', '1979-09-17');
INSERT INTO users (id, name, userName, dob) VALUES ('35', 'James', 'Carlile', '1990-06-25');
INSERT INTO users (id, name, userName, dob) VALUES ('36', 'Lyndsey', 'Drinkel', '1956-12-19');
INSERT INTO users (id, name, userName, dob) VALUES ('37', 'Harley', 'Leftbridge', '1972-03-07');
INSERT INTO users (id, name, userName, dob) VALUES ('38', 'Benito', 'McQuillen', '1951-10-11');
INSERT INTO users (id, name, userName, dob) VALUES ('39', 'Walliw', 'Harmeston', '1985-05-29');
INSERT INTO users (id, name, userName, dob) VALUES ('40', 'Farica', 'Duguid', '1948-01-20');
INSERT INTO users (id, name, userName, dob) VALUES ('41', 'Nichols', 'Christofol', '1945-12-18');
INSERT INTO users (id, name, userName, dob) VALUES ('42', 'Nora', 'Weatherill', '1984-02-07');
INSERT INTO users (id, name, userName, dob) VALUES ('43', 'Thea', 'Tale', '1980-10-01');
INSERT INTO users (id, name, userName, dob) VALUES ('44', 'Burty', 'Treadway', '1958-04-04');
INSERT INTO users (id, name, userName, dob) VALUES ('45', 'Vivia', 'Brunroth', '1963-08-17');
INSERT INTO users (id, name, userName, dob) VALUES ('46', 'Janel', 'Gosnall', '1940-05-16');
INSERT INTO users (id, name, userName, dob) VALUES ('47', 'Heidi', 'Anderl', '1943-08-02');
INSERT INTO users (id, name, userName, dob) VALUES ('48', 'Edlin', 'Drinkall', '2002-10-29');
INSERT INTO users (id, name, userName, dob) VALUES ('49', 'Josselyn', 'Danbye', '1986-12-01');
INSERT INTO users (id, name, userName, dob) VALUES ('50', 'Mora', 'Mewhirter', '1988-01-06');

INSERT INTO volunteers (id, name) VALUES ('1', 'Jena Vaisey');
INSERT INTO volunteers (id, name) VALUES ('2', 'Bianka O''Sullivan');
INSERT INTO volunteers (id, name) VALUES ('3', 'Loreen Daldry');
INSERT INTO volunteers (id, name) VALUES ('4', 'Cristobal Rouzet');
INSERT INTO volunteers (id, name) VALUES ('5', 'Dicky Gaylord');
INSERT INTO volunteers (id, name) VALUES ('6', 'Smith Najara');
INSERT INTO volunteers (id, name) VALUES ('7', 'Bronny Livermore');
INSERT INTO volunteers (id, name) VALUES ('8', 'Reeba Commuzzo');
INSERT INTO volunteers (id, name) VALUES ('9', 'Kara Pinke');
INSERT INTO volunteers (id, name) VALUES ('10', 'Jerrome Roust');
INSERT INTO volunteers (id, name) VALUES ('11', 'Justinian Tattersill');
INSERT INTO volunteers (id, name) VALUES ('12', 'Rheba Bulluck');
INSERT INTO volunteers (id, name) VALUES ('13', 'Loreen Fogden');
INSERT INTO volunteers (id, name) VALUES ('14', 'Ninnetta Suter');
INSERT INTO volunteers (id, name) VALUES ('15', 'Edy Imrie');
INSERT INTO volunteers (id, name) VALUES ('16', 'Alon Tratton');
INSERT INTO volunteers (id, name) VALUES ('17', 'Hube Zmitrichenko');
INSERT INTO volunteers (id, name) VALUES ('18', 'Ali Shevill');
INSERT INTO volunteers (id, name) VALUES ('19', 'Lewie Matissoff');
INSERT INTO volunteers (id, name) VALUES ('20', 'Oran Kennifeck');
INSERT INTO volunteers (id, name) VALUES ('21', 'Blondell McCoughan');
INSERT INTO volunteers (id, name) VALUES ('22', 'Beverlee Blinerman');
INSERT INTO volunteers (id, name) VALUES ('23', 'Gelya Penning');
INSERT INTO volunteers (id, name) VALUES ('24', 'Dolf Dorow');
INSERT INTO volunteers (id, name) VALUES ('25', 'Marmaduke Janczewski');
INSERT INTO volunteers (id, name) VALUES ('26', 'Rolph Corbin');
INSERT INTO volunteers (id, name) VALUES ('27', 'Yvor Grigorescu');
INSERT INTO volunteers (id, name) VALUES ('28', 'Cecilius Cato');
INSERT INTO volunteers (id, name) VALUES ('29', 'Josee Ladlow');
INSERT INTO volunteers (id, name) VALUES ('30', 'Alysa Takle');

INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('1', '2023-10-25', '1', 'Legal', 'Wednesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('2', '2024-02-11', '2', 'Training', 'Sunday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('3', '2023-08-14', '3', 'Business Development', 'Monday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('4', '2023-08-21', '4', 'Research and Development', 'Monday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('5', '2023-09-07', '5', 'Legal', 'Thursday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('6', '2024-05-22', '6', 'Research and Development', 'Wednesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('7', '2024-02-06', '7', 'Training', 'Tuesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('8', '2024-02-25', '8', 'Services', 'Sunday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('9', '2023-09-12', '9', 'Human Resources', 'Tuesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('10', '2024-02-01', '10', 'Support', 'Thursday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('12', '2023-07-28', '11', 'Legal', 'Friday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('13', '2024-03-01', '12', 'Research and Development', 'Friday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('14', '2023-08-09', '13', 'Business Development', 'Wednesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('15', '2023-06-05', '14', 'Engineering', 'Monday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('16', '2023-12-13', '15', 'Training', 'Wednesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('17', '2023-08-26', '16', 'Research and Development', 'Saturday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('18', '2023-12-30', '17', 'Sales', 'Saturday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('19', '2024-02-26', '18', 'Research and Development', 'Monday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('20', '2024-02-01', '19', 'Services', 'Thursday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('21', '2023-10-28', '20', 'Training', 'Saturday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('22', '2023-10-02', '21', 'Training', 'Monday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('23', '2023-12-09', '22', 'Training', 'Saturday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('24', '2024-01-24', '23', 'Marketing', 'Wednesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('25', '2023-08-14', '24', 'Accounting', 'Monday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('26', '2023-11-10', '25', 'Accounting', 'Friday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('27', '2024-02-06', '26', 'Legal', 'Tuesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('28', '2023-10-30', '27', 'Marketing', 'Monday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('29', '2023-09-12', '28', 'Business Development', 'Tuesday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('30', '2023-09-24', '29', 'Support', 'Sunday');
INSERT INTO appointments (volunteerID, appDate, appointmentID, subject, weekday) VALUES ('1', '2023-08-22', '30', 'Product Management', 'Tuesday');

INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('1', '175', 'et', '3', '2024-01-31');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('2', '88', 'sit amet', '5', '2023-11-27');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('3', '64', 'neque', '1', '2023-11-12');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('4', '34', 'quam sollicitudin', '3', '2024-04-08');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('5', '159', 'dolor quis', '3', '2023-11-23');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('6', '32', 'tristique', '6', '2023-08-24');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('7', '49', 'felis', '2', '2023-10-25');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('8', '25', 'blandit non', '3', '2023-06-19');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('9', '133', 'nascetur', '5', '2024-02-04');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('10', '166', 'in', '6', '2023-06-27');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('11', '71', 'in felis', '5', '2024-02-27');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('12', '165', 'id', '8', '2023-07-22');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('13', '167', 'curae nulla', '8', '2023-12-18');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('14', '73', 'tortor', '5', '2023-11-07');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('15', '12', 'placerat praesent', '8', '2023-12-01');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('16', '115', 'ac diam', '8', '2024-03-26');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('17', '3', 'posuere', '7', '2023-11-06');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('18', '102', 'maecenas', '5', '2023-11-08');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('19', '36', 'orci', '4', '2023-10-22');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('20', '27', 'est', '3', '2023-12-28');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('21', '69', 'pellentesque viverra', '1', '2023-10-10');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('22', '96', 'lacus at', '8', '2023-12-29');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('23', '72', 'faucibus orci', '7', '2023-11-05');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('24', '75', 'tortor', '5', '2023-11-02');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('25', '23', 'odio', '1', '2024-05-11');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('26', '115', 'porttitor', '1', '2024-05-24');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('27', '107', 'dui proin', '5', '2023-09-26');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('28', '140', 'ante vivamus', '7', '2024-04-05');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('29', '150', 'quam', '7', '2023-06-10');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('30', '9', 'imperdiet', '1', '2023-06-21');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('31', '181', 'amet sem', '7', '2023-10-27');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('32', '67', 'justo etiam', '6', '2023-12-06');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('33', '44', 'sit amet', '2', '2024-06-01');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('34', '11', 'a', '2', '2023-11-22');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('35', '166', 'sed', '6', '2023-07-31');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('36', '58', 'in felis', '5', '2023-09-27');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('37', '183', 'sapien', '6', '2023-11-15');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('38', '84', 'turpis', '5', '2024-02-03');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('39', '71', 'tristique', '8', '2024-02-01');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('40', '166', 'venenatis non', '3', '2024-04-18');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('41', '162', 'pulvinar sed', '7', '2023-09-17');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('42', '182', 'ligula', '2', '2024-05-12');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('43', '180', 'mattis', '1', '2024-02-02');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('44', '17', 'libero', '8', '2024-04-01');
INSERT INTO communityEvent (eventID, venueCapacity, name, duration, eventDate) VALUES ('45', '14', 'sed vestibulum', '8', '2024-04-12');


INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('1', '23', 'Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis. Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', 'nulla', '2023-09-17');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('2', '15', 'In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.', 'ullamcorper', '2024-01-25');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('3', '31', 'Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.', 'luctus', '2023-06-05');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('4', '7', 'Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat. Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus.', 'id', '2024-03-10');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('5', '2', 'Proin at turpis a pede posuere nonummy. Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl.', 'vulputate', '2023-09-18');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('6', '37', 'Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros.', 'sit', '2023-11-15');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('7', '45', 'Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat. Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa.', 'justo', '2023-07-31');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('8', '24', 'Fusce consequat. Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa.', 'non', '2024-04-02');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('9', '46', 'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque.', 'neque', '2024-03-06');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('10', '34', 'Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.', 'turpis', '2024-05-07');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('11', '8', 'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo.', 'tempor', '2023-11-20');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('12', '47', 'Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti.', 'aliquet', '2024-02-23');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('13', '5', 'Duis aliquam convallis nunc.', 'vulputate', '2023-09-01');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('14', '10', 'Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat. Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa.', 'parturient', '2024-02-12');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('15', '12', 'In eleifend quam a odio. In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat. Curabitur gravida nisi at nibh.', 'posuere', '2024-05-06');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('16', '41', 'Maecenas pulvinar lobortis est.', 'sapien', '2024-05-24');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('17', '42', 'Fusce consequat. Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum. In hac habitasse platea dictumst.', 'curabitur', '2023-11-04');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('18', '36', 'Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi. Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque. Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus. Phasellus in felis.', 'dui', '2024-04-25');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('19', '44', 'Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam.', 'pede', '2024-05-10');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('20', '18', 'Duis at velit eu est congue elementum. In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo. Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis. Sed ante. Vivamus tortor. Duis mattis egestas metus.', 'pede', '2023-12-25');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('21', '6', 'Proin risus. Praesent lectus. Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis. Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', 'turpis', '2024-03-13');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('22', '50', 'Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi. Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit.', 'proin', '2023-08-16');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('23', '48', 'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo.', 'congue', '2024-02-18');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('24', '49', 'Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus. Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi. Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.', 'odio', '2023-06-12');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('25', '20', 'Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue.', 'eu', '2024-04-13');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('26', '38', 'Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum. In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo. Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros.', 'id', '2024-03-04');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('27', '32', 'Vivamus tortor. Duis mattis egestas metus.', 'in', '2023-10-23');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('28', '1', 'Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.', 'non', '2023-07-19');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('29', '29', 'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci.', 'nunc', '2023-10-06');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('30', '35', 'Nunc purus. Phasellus in felis. Donec semper sapien a libero. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.', 'dolor', '2023-11-02');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('31', '22', 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros. Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat. In congue. Etiam justo. Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna.', 'odio', '2023-09-09');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('32', '19', 'Sed ante.', 'nisl', '2024-02-16');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('33', '17', 'Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh.', 'sit', '2024-05-23');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('34', '9', 'Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.', 'sem', '2024-04-19');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('35', '40', 'In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum.', 'platea', '2023-06-29');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('36', '21', 'Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum. Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.', 'justo', '2024-04-09');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('37', '4', 'Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.', 'quam', '2024-04-27');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('38', '3', 'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl.', 'est', '2023-12-03');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('39', '28', 'Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.', 'pellentesque', '2023-09-29');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('40', '16', 'Duis bibendum.', 'tempus', '2024-03-25');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('41', '39', 'Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo.', 'vitae', '2023-12-19');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('42', '11', 'Aliquam erat volutpat. In congue. Etiam justo. Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus. Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.', 'amet', '2024-05-19');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('43', '13', 'Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti. Nullam porttitor lacus at turpis.', 'morbi', '2023-10-01');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('44', '30', 'Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.', 'vestibulum', '2023-06-26');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('45', '26', 'Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.', 'dui', '2024-05-15');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('46', '33', 'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh.', 'pellentesque', '2023-11-17');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('47', '14', 'Donec semper sapien a libero. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius. Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus.', 'ac', '2023-06-26');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('48', '27', 'Phasellus in felis. Donec semper sapien a libero. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius. Integer ac leo. Pellentesque ultrices mattis odio.', 'aliquam', '2024-05-04');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('49', '43', 'Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem. Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.', 'adipiscing', '2024-05-08');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('50', '25', 'Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia.', 'mauris', '2023-12-16');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('51', '5', 'Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue.', 'diam', '2023-08-14');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('52', '14', 'Nunc rhoncus dui vel sem. Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus. Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.', 'dolor', '2023-06-13');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('53', '30', 'Maecenas tincidunt lacus at velit.', 'duis', '2023-09-26');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('54', '3', 'Donec ut mauris eget massa tempor convallis.', 'quisque', '2024-05-22');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('55', '35', 'Nulla facilisi. Cras non velit nec nisi vulputate nonummy.', 'nunc', '2023-06-16');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('56', '40', 'Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus. Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', 'iaculis', '2024-01-02');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('57', '25', 'Duis at velit eu est congue elementum.', 'sed', '2024-03-21');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('58', '1', 'Suspendisse accumsan tortor quis turpis. Sed ante. Vivamus tortor. Duis mattis egestas metus.', 'quis', '2023-08-27');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('59', '42', 'Fusce consequat. Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum. In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.', 'vestibulum', '2024-04-11');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('60', '15', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl. Aenean lectus.', 'cras', '2024-04-14');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('61', '28', 'Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo.', 'dis', '2023-07-21');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('62', '20', 'Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl. Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.', 'tortor', '2024-01-31');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('63', '33', 'Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.', 'vitae', '2023-10-07');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('64', '29', 'Fusce consequat. Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.', 'est', '2023-06-17');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('65', '47', 'Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices.', 'eros', '2023-12-22');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('66', '49', 'Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo. Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis. Sed ante. Vivamus tortor. Duis mattis egestas metus. Aenean fermentum.', 'ullamcorper', '2024-01-18');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('67', '39', 'Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum. In hac habitasse platea dictumst.', 'id', '2023-09-24');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('68', '4', 'Morbi a ipsum. Integer a nibh.', 'ante', '2023-10-16');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('69', '9', 'In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.', 'aenean', '2023-12-13');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('70', '27', 'Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.', 'cras', '2023-12-02');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('71', '38', 'Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt.', 'vulputate', '2024-03-09');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('72', '43', 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti. Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris. Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus.', 'montes', '2024-01-31');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('73', '17', 'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo.', 'ipsum', '2024-04-07');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('74', '46', 'Vivamus vel nulla eget eros elementum pellentesque.', 'odio', '2024-02-01');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('75', '26', 'Ut at dolor quis odio consequat varius. Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.', 'orci', '2023-12-13');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('76', '7', 'Nulla nisl.', 'ipsum', '2023-11-23');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('77', '12', 'Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem. Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus. Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien.', 'velit', '2023-07-03');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('78', '10', 'Curabitur convallis. Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus. Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.', 'auctor', '2024-02-13');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('79', '31', 'Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum.', 'justo', '2024-02-19');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('80', '2', 'Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo.', 'duis', '2023-09-25');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('81', '6', 'Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl.', 'amet', '2023-06-13');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('82', '34', 'Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue.', 'bibendum', '2023-06-12');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('83', '22', 'In congue. Etiam justo. Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus. Nulla ut erat id mauris vulputate elementum. Nullam varius.', 'maecenas', '2024-01-21');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('84', '11', 'Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue.', 'tempus', '2023-09-05');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('85', '18', 'Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus. Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue.', 'feugiat', '2024-04-02');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('86', '16', 'Phasellus in felis. Donec semper sapien a libero. Nam dui.', 'nunc', '2023-12-19');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('87', '45', 'Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue.', 'odio', '2023-07-22');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('88', '13', 'Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.', 'morbi', '2024-05-15');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('89', '50', 'Duis at velit eu est congue elementum. In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante.', 'nonummy', '2023-07-02');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('90', '23', 'Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy.', 'donec', '2023-06-05');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('91', '44', 'Aliquam non mauris.', 'aliquam', '2024-03-13');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('92', '32', 'Morbi a ipsum. Integer a nibh.', 'lectus', '2024-01-12');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('93', '8', 'Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.', 'vitae', '2024-03-29');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('94', '37', 'Nulla suscipit ligula in lacus. Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', 'purus', '2023-07-30');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('95', '21', 'Nunc rhoncus dui vel sem. Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci.', 'tellus', '2023-07-18');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('96', '41', 'Nulla tempus. Vivamus in felis eu sapien cursus vestibulum. Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.', 'odio', '2023-07-18');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('97', '36', 'Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.', 'justo', '2023-10-14');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('98', '19', 'Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl.', 'non', '2024-03-24');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('99', '24', 'In eleifend quam a odio. In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat. Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.', 'est', '2023-12-22');
INSERT INTO posts (postID, migrantID, postContent, displayName, createdAt) VALUES ('100', '48', 'Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.', 'dapibus', '2024-02-11');

DROP TABLE IF EXISTS model1_params;
CREATE TABLE IF NOT EXISTS model1_params (
    beta_vals LONGTEXT
);
INSERT INTO model1_params (beta_vals) VALUES ('[ -11.189063, 0.00657606, -1.77841744, -1.2832241 , -2.12463282, -2.33197343,
       -2.18232304, -1.6609086 , -1.26502699, -2.04542162, -2.27506478,
       -2.2812903 , -1.26957965, -2.05973826, -1.32056226,  0.28477442,
       -2.10320113, -1.75817804, -2.2829184 , -2.03031371, -1.35753525,
       -2.03546333, -1.636657  , -0.96578071, -2.01102748, -2.32092311,
       -2.20148675, -1.00011601, -0.52893714, -2.3135955 , -1.82623765,
       -0.60812822, -1.20680105, -2.20299596, -0.82739702, -0.13280885,
       -1.97478515, -1.81217596, -1.85404245, -2.09568796, -1.7802394 ,
       -1.77191663, -0.36780429, -2.05343349, -1.24497814, -1.83085538,
       -1.83027334, -2.02920071, -2.28660117, -2.27034977,  0.51106508,
       -2.28387902,  0.06222744, -1.53372582, -1.76367056, -0.58455716,
       -1.96097165, -0.45231696, -2.21591496, -1.39806335,  1.05869968,
       -2.09720948, -2.28272537, -2.28386038, -1.28165523, -0.6040314 ,
       -1.37433571,  0.36101178, -0.91010364, -2.28972179, -2.22610491,
       -1.4621265 , -1.10673551, -1.49016867, -2.12797223, -2.17667094,
       -2.11367469, -2.27756578, -2.27868523, -1.03048449, -0.88896513,
       -0.20364972, -0.19893764, -1.62508871, -2.26656465, -2.28636496,
       -2.07366698, -2.27262915, -0.797841  , -1.1362499 ,  0.44468015,
       -1.5074468 , -1.35147764, -2.19073955, -1.05413698, -1.80750465,
       -1.18695712,  0.02929037, -2.26236722, -2.20150737, -2.29073967,
       -1.83515616, -0.03214214, -0.87582788, -0.42332612, -2.28438321,
       -1.12566324, -2.08040659, -1.5084294 , -2.05747447, -2.31206359,
       -2.09410999, -1.40317556, -2.06061412, -1.25350977, -0.58217869,
       -2.32094033, -1.11096476, -2.02860469, -0.6540188 , -2.28397919,
       -2.28035187, -1.61805904, -0.68575394, -0.97086375, -1.58870176,
       -2.28266556, -1.18022079, -0.8013649 , -1.89431212, -2.0101317 ,
       -1.85495622, -2.05710993, -1.83085142, -2.27142582, -2.28747581,
       -1.63774263, -1.84742112, -1.92146101, -1.80673563, -2.28136897,
       -0.25786747, -2.24629711, -2.09664658, -2.29531637, -2.04621335,
       -1.59948816, -1.10126917, -1.66697084, -0.84480584, -2.22635614,
       -2.06311699, -2.24297025, -2.05568837, -2.15743053, -0.74153378,
       -1.91978298,  1.91550769, -2.28693232, -1.31203597,  0.59764416,
       -2.05031715, -2.28202682, -0.9464864 , -1.00798072, -1.37611709,
       -0.72180175, -2.0940014 , -0.82642367, -2.02905792, -1.47871402,
       -1.95709553, -2.08224367, -0.68022212,  0.98842482, -2.0364671 ,
       -1.33945118, -2.28598868,  0.93840192, -2.14141969, -1.74854516,
       -1.40999911, -2.13236155, -1.7600597 , -2.29060771,  0.09955894,
       -0.1761455 , -0.86527773,  0.06847763,  0.10816341,  0.74590844,
        0.1248014 , -0.12657619]');

DROP TABLE IF EXISTS country_table;
CREATE TABLE country_table (
  index_num BIGINT,
  country VARCHAR(1024)
);

INSERT INTO country_table (index_num, country) VALUES (0, 'Albania');
INSERT INTO country_table (index_num, country) VALUES (1,'Algeria');
INSERT INTO country_table (index_num, country) VALUES(2,'Angola');
INSERT INTO country_table (index_num, country) VALUES (3,'Anguilla');
INSERT INTO country_table (index_num, country) VALUES (4,'Antigua and Barbuda');
INSERT INTO country_table (index_num, country) VALUES (5,'Argentina');
INSERT INTO country_table (index_num, country) VALUES (6,'Armenia');
INSERT INTO country_table (index_num, country) VALUES (7,'Aruba');
INSERT INTO country_table (index_num, country) VALUES (8,'Australia');
INSERT INTO country_table (index_num, country) VALUES (9,'Austria');
INSERT INTO country_table (index_num, country) VALUES (10,'Azerbaijan');
INSERT INTO country_table (index_num, country) VALUES (11,'Bahamas');
INSERT INTO country_table (index_num, country) VALUES (12,'Bahrain');
INSERT INTO country_table (index_num, country) VALUES (13,'Bangladesh');
INSERT INTO country_table (index_num, country) VALUES (14,'Barbados');
INSERT INTO country_table (index_num, country) VALUES (15,'Belarus');
INSERT INTO country_table (index_num, country) VALUES (16,'Belgium');
INSERT INTO country_table (index_num, country) VALUES (17,'Belize');
INSERT INTO country_table (index_num, country) VALUES (18,'Benin');
INSERT INTO country_table (index_num, country) VALUES (19,'Bolivia, Plurinational State of)');
INSERT INTO country_table (index_num, country) VALUES (20,'Bosnia and Herzegovina');
INSERT INTO country_table (index_num, country) VALUES (21,'Botswana');
INSERT INTO country_table (index_num, country) VALUES (22,'Brazil');
INSERT INTO country_table (index_num, country) VALUES (23,'Brunei Darussalam');
INSERT INTO country_table (index_num, country) VALUES (24,'Bulgaria');
INSERT INTO country_table (index_num, country) VALUES (25,'Burkina Faso');
INSERT INTO country_table (index_num, country) VALUES (26,'Burundi');
INSERT INTO country_table (index_num, country) VALUES (27,'Cabo Verde');
INSERT INTO country_table (index_num, country) VALUES (28,'Cambodia');
INSERT INTO country_table (index_num, country) VALUES (29,'Cameroon');
INSERT INTO country_table (index_num, country) VALUES (30,'Canada');
INSERT INTO country_table (index_num, country) VALUES (31,'Cayman Islands');
INSERT INTO country_table (index_num, country) VALUES (32,'Central African Rep.');
INSERT INTO country_table (index_num, country) VALUES (33,'Chad');
INSERT INTO country_table (index_num, country) VALUES (34,'Chile');
INSERT INTO country_table (index_num, country) VALUES (35,'China');
INSERT INTO country_table (index_num, country) VALUES (36,'China, Hong Kong SAR');
INSERT INTO country_table (index_num, country) VALUES (37,'China, Macao SAR');
INSERT INTO country_table (index_num, country) VALUES (38,'Colombia');
INSERT INTO country_table (index_num, country) VALUES (39,'Comoros');
INSERT INTO country_table (index_num, country) VALUES (40,'Congo');
INSERT INTO country_table (index_num, country) VALUES (41,'Costa Rica');
INSERT INTO country_table (index_num, country) VALUES (42,'Cote d''Ivoire');
INSERT INTO country_table (index_num, country) VALUES (43,'Croatia');
INSERT INTO country_table (index_num, country) VALUES (44,'Cuba');
INSERT INTO country_table (index_num, country) VALUES (45,'Curacao');
INSERT INTO country_table (index_num, country) VALUES (46,'Cyprus');
INSERT INTO country_table (index_num, country) VALUES (47,'Czechia');
INSERT INTO country_table (index_num, country) VALUES (48,'Dem. Rep. of the Congo');
INSERT INTO country_table (index_num, country) VALUES (49,'Denmark');
INSERT INTO country_table (index_num, country) VALUES (50,'Djibouti');
INSERT INTO country_table (index_num, country) VALUES (51,'Dominican Rep.');
INSERT INTO country_table (index_num, country) VALUES (52,'Ecuador');
INSERT INTO country_table (index_num, country) VALUES (53,'Egypt');
INSERT INTO country_table (index_num, country) VALUES (54,'El Salvador');
INSERT INTO country_table (index_num, country) VALUES (55,'Eritrea');
INSERT INTO country_table (index_num, country) VALUES (56,'Estonia');
INSERT INTO country_table (index_num, country) VALUES (57,'Eswatini');
INSERT INTO country_table (index_num, country) VALUES (58,'Ethiopia');
INSERT INTO country_table (index_num, country) VALUES (59,'Fiji');
INSERT INTO country_table (index_num, country) VALUES (60,'Finland');
INSERT INTO country_table (index_num, country) VALUES (61,'France');
INSERT INTO country_table (index_num, country) VALUES (62,'Gabon');
INSERT INTO country_table (index_num, country) VALUES (63,'Gambia');
INSERT INTO country_table (index_num, country) VALUES (64,'Georgia');
INSERT INTO country_table (index_num, country) VALUES (65,'Germany');
INSERT INTO country_table (index_num, country) VALUES (66,'Ghana');
INSERT INTO country_table (index_num, country) VALUES (67,'Greece');
INSERT INTO country_table (index_num, country) VALUES (68,'Grenada');
INSERT INTO country_table (index_num, country) VALUES (69,'Guatemala');
INSERT INTO country_table (index_num, country) VALUES (70,'Guinea');
INSERT INTO country_table (index_num, country) VALUES (71,'Guinea-Bissau');
INSERT INTO country_table (index_num, country) VALUES (72,'Guyana');
INSERT INTO country_table (index_num, country) VALUES (73,'Haiti');
INSERT INTO country_table (index_num, country) VALUES (74,'Honduras');
INSERT INTO country_table (index_num, country) VALUES (75,'Hungary');
INSERT INTO country_table (index_num, country) VALUES (76,'Iceland');
INSERT INTO country_table (index_num, country) VALUES (77,'India');
INSERT INTO country_table (index_num, country) VALUES (78,'Indonesia');
INSERT INTO country_table (index_num, country) VALUES (79,'Iran, Islamic Rep. of)');
INSERT INTO country_table (index_num, country) VALUES (80,'Iraq');
INSERT INTO country_table (index_num, country) VALUES (81,'Ireland');
INSERT INTO country_table (index_num, country) VALUES (82,'Israel');
INSERT INTO country_table (index_num, country) VALUES (83,'Italy');
INSERT INTO country_table (index_num, country) VALUES (84,'Jamaica');
INSERT INTO country_table (index_num, country) VALUES (85,'Japan');
INSERT INTO country_table (index_num, country) VALUES (86,'Jordan');
INSERT INTO country_table (index_num, country) VALUES (87,'Kazakhstan');
INSERT INTO country_table (index_num, country) VALUES (88,'Kenya');
INSERT INTO country_table (index_num, country) VALUES (89,'Kuwait');
INSERT INTO country_table (index_num, country) VALUES (90,'Kyrgyzstan');
INSERT INTO country_table (index_num, country) VALUES (91,'Latvia');
INSERT INTO country_table (index_num, country) VALUES (92,'Lebanon');
INSERT INTO country_table (index_num, country) VALUES (93,'Lesotho');
INSERT INTO country_table (index_num, country) VALUES (94,'Liberia');
INSERT INTO country_table (index_num, country) VALUES (95,'Libya');
INSERT INTO country_table (index_num, country) VALUES (96,'Liechtenstein');
INSERT INTO country_table (index_num, country) VALUES (97,'Lithuania');
INSERT INTO country_table (index_num, country) VALUES (98,'Luxembourg');
INSERT INTO country_table (index_num, country) VALUES (99,'Madagascar');
INSERT INTO country_table (index_num, country) VALUES (100,'Malawi');
INSERT INTO country_table (index_num, country) VALUES (101,'Malaysia');
INSERT INTO country_table (index_num, country) VALUES (102,'Mali');
INSERT INTO country_table (index_num, country) VALUES (103,'Malta');
INSERT INTO country_table (index_num, country) VALUES (104,'Mauritania');
INSERT INTO country_table (index_num, country) VALUES (105,'Mauritius');
INSERT INTO country_table (index_num, country) VALUES (106,'Mexico');
INSERT INTO country_table (index_num, country) VALUES (107,'Micronesia, Federated States of');
INSERT INTO country_table (index_num, country) VALUES (108,'Monaco');
INSERT INTO country_table (index_num, country) VALUES (109,'Mongolia');
INSERT INTO country_table (index_num, country) VALUES (110,'Montenegro');
INSERT INTO country_table (index_num, country) VALUES (111,'Montserrat');
INSERT INTO country_table (index_num, country) VALUES (112,'Morocco');
INSERT INTO country_table (index_num, country) VALUES (113,'Mozambique');
INSERT INTO country_table (index_num, country) VALUES (114,'Myanmar');
INSERT INTO country_table (index_num, country) VALUES (115,'Namibia');
INSERT INTO country_table (index_num, country) VALUES (116,'Nauru');
INSERT INTO country_table (index_num, country) VALUES (117,'Nepal');
INSERT INTO country_table (index_num, country) VALUES (118,'Netherlands, Kingdom of the');
INSERT INTO country_table (index_num, country) VALUES (119,'New Zealand');
INSERT INTO country_table (index_num, country) VALUES (120,'Nicaragua');
INSERT INTO country_table (index_num, country) VALUES (121,'Niger');
INSERT INTO country_table (index_num, country) VALUES (122,'Nigeria');
INSERT INTO country_table (index_num, country) VALUES (123,'North Macedonia');
INSERT INTO country_table (index_num, country) VALUES (124,'Norway');
INSERT INTO country_table (index_num, country) VALUES (125,'Oman');
INSERT INTO country_table (index_num, country) VALUES (126,'Pakistan');
INSERT INTO country_table (index_num, country) VALUES (127,'Panama');
INSERT INTO country_table (index_num, country) VALUES (128,'Papua New Guinea');
INSERT INTO country_table (index_num, country) VALUES (129,'Paraguay');
INSERT INTO country_table (index_num, country) VALUES (130,'Peru');
INSERT INTO country_table (index_num, country) VALUES (131,'Philippines');
INSERT INTO country_table (index_num, country) VALUES (132,'Poland');
INSERT INTO country_table (index_num, country) VALUES (133,'Portugal');
INSERT INTO country_table (index_num, country) VALUES (134,'Qatar');
INSERT INTO country_table (index_num, country) VALUES (135,'Rep. of Korea');
INSERT INTO country_table (index_num, country) VALUES (136,'Rep. of Moldova');
INSERT INTO country_table (index_num, country) VALUES (137,'Romania');
INSERT INTO country_table (index_num, country) VALUES (138,'Russian Federation');
INSERT INTO country_table (index_num, country) VALUES (139,'Rwanda');
INSERT INTO country_table (index_num, country) VALUES (140,'Saint Kitts and Nevis');
INSERT INTO country_table (index_num, country) VALUES (141,'Saint Lucia');
INSERT INTO country_table (index_num, country) VALUES (142,'Saint Vincent and the Grenadines');
INSERT INTO country_table (index_num, country) VALUES (143,'Samoa');
INSERT INTO country_table (index_num, country) VALUES (144,'Saudi Arabia');
INSERT INTO country_table (index_num, country) VALUES (145,'Senegal');
INSERT INTO country_table (index_num, country) VALUES (146,'Serbia and Kosovo: (1999)');
INSERT INTO country_table (index_num, country) VALUES (147,'Sierra Leone');
INSERT INTO country_table (index_num, country) VALUES (148,'Singapore');
INSERT INTO country_table (index_num, country) VALUES (149,'Sint Maarten, Dutch part');
INSERT INTO country_table (index_num, country) VALUES (150,'Slovakia');
INSERT INTO country_table (index_num, country) VALUES (151,'Slovenia');
INSERT INTO country_table (index_num, country) VALUES (152,'Solomon Islands');
INSERT INTO country_table (index_num, country) VALUES (153,'Somalia');
INSERT INTO country_table (index_num, country) VALUES (154,'South Africa');
INSERT INTO country_table (index_num, country) VALUES (155,'South Sudan');
INSERT INTO country_table (index_num, country) VALUES (156,'Spain');
INSERT INTO country_table (index_num, country) VALUES (157,'Sri Lanka');
INSERT INTO country_table (index_num, country) VALUES (158,'Sudan');
INSERT INTO country_table (index_num, country) VALUES (159,'Suriname');
INSERT INTO country_table (index_num, country) VALUES (160,'Sweden');
INSERT INTO country_table (index_num, country) VALUES (161,'Switzerland');
INSERT INTO country_table (index_num, country) VALUES (162,'Syrian Arab Rep.');
INSERT INTO country_table (index_num, country) VALUES (163,'Tajikistan');
INSERT INTO country_table (index_num, country) VALUES (164,'Thailand');
INSERT INTO country_table (index_num, country) VALUES (165,'Timor-Leste');
INSERT INTO country_table (index_num, country) VALUES (166,'Togo');
INSERT INTO country_table (index_num, country) VALUES (167,'Trinidad and Tobago');
INSERT INTO country_table (index_num, country) VALUES (168,'Tunisia');
INSERT INTO country_table (index_num, country) VALUES (169,'Turkmenistan');
INSERT INTO country_table (index_num, country) VALUES (170,'Turks and Caicos Islands');
INSERT INTO country_table (index_num, country) VALUES (171,'Türkiye');
INSERT INTO country_table (index_num, country) VALUES (172,'Uganda');
INSERT INTO country_table (index_num, country) VALUES (173,'Ukraine');
INSERT INTO country_table (index_num, country) VALUES (174,'United Arab Emirates');
INSERT INTO country_table (index_num, country) VALUES (175,'United Kingdom of Great Britain and Northern Ireland');
INSERT INTO country_table (index_num, country) VALUES (176,'United Rep. of Tanzania');
INSERT INTO country_table (index_num, country) VALUES (177,'United States of America');
INSERT INTO country_table (index_num, country) VALUES (178,'Uruguay');
INSERT INTO country_table (index_num, country) VALUES (179,'Uzbekistan');
INSERT INTO country_table (index_num, country) VALUES (180,'Vanuatu');
INSERT INTO country_table (index_num, country) VALUES (181,'Venezuela, Bolivarian Republic of');
INSERT INTO country_table (index_num, country) VALUES (182,'Viet Nam');
INSERT INTO country_table (index_num, country) VALUES (183,'Yemen');
INSERT INTO country_table (index_num, country) VALUES (184,'Zambia');
INSERT INTO country_table (index_num, country) VALUES (185,'Zimbabwe');

INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('1', '12');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('1', '13');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('2', '15');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('3', '14');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('4', '25');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('4', '16');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('4', '8');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('5', '27');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('3', '2');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('5', '40');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('7', '50');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('18', '1');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('23', '9');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('19', '38');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('10', '41');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('25', '19');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('18', '3');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('17', '23');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('4', '22');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('3', '36');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('21', '20');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('27', '31');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('30', '11');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('18', '29');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('17', '28');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('27', '39');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('19', '30');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('30', '18');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('16', '26');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('20', '6');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('11', '7');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('5', '48');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('15', '34');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('9', '21');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('13', '10');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('30', '17');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('28', '37');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('14', '49');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('26', '42');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('14', '44');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('12', '33');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('25', '5');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('23', '47');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('19', '43');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('23', '35');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('27', '45');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('5', '4');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('18', '32');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('12', '46');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('29', '24');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('27', '22');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('5', '1');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('1', '18');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('12', '1');
INSERT INTO appointmentAttendees (appointmentID, attendeeID) VALUES ('29', '12');

