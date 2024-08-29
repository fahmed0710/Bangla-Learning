USE banglalearning;

--add a word example for english equiv pronounciation?
CREATE TABLE Consonants(
  consonant_id INT PRIMARY KEY NOT NULL UNIQUE,
  consonant VARCHAR(2) NOT NULL,
  english_pronounciation VARCHAR(5) NOT NULL,
  audio_path VARCHAR(25) NOT NULL
);

CREATE TABLE Vowels(
  vowel_id INT PRIMARY KEY NOT NULL UNIQUE,
  vowel VARCHAR(2) NOT NULL,
  english_pronounciation VARCHAR(5) NOT NULL,
  diacritic VARCHAR(5),
  audio_path VARCHAR(25) NOT NULL
);

CREATE TABLE Conjuncts(
  conjunct_id INT PRIMARY KEY NOT NULL UNIQUE,
  conjunct VARCHAR(2) NOT NULL,
  part_1 VARCHAR(2) NOT NULL,
  part_2 VARCHAR(2) NOT NULL
);