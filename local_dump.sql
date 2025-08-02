--
-- PostgreSQL database dump
--

-- Dumped from database version 15.13 (Homebrew)
-- Dumped by pg_dump version 15.13 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

-- *not* creating schema, since initdb creates it


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: all_movies; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.all_movies (
    movie_id integer NOT NULL,
    title text NOT NULL,
    overview text NOT NULL,
    poster text NOT NULL,
    vote real NOT NULL,
    release_date date NOT NULL
);


--
-- Name: all_reviews; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.all_reviews (
    movie_id integer NOT NULL,
    username text NOT NULL,
    rating real NOT NULL,
    review text NOT NULL
);


--
-- Data for Name: all_movies; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.all_movies (movie_id, title, overview, poster, vote, release_date) FROM stdin;
8871	How the Grinch Stole Christmas	The Grinch decides to rob Whoville of Christmas - but a dash of kindness from little Cindy Lou Who and her family may be enough to melt his heart...	https://image.tmdb.org/t/p/w1280/AmUs3hximCKa90sHuIRr5Bz8ci5.jpg	6.8	2000-11-17
402431	Wicked	In the land of Oz, ostracized and misunderstood green-skinned Elphaba is forced to share a room with the popular aristocrat Glinda at Shiz University, and the two's unlikely friendship is tested as they begin to fulfill their respective destinies as Glinda the Good and the Wicked Witch of the West.	https://image.tmdb.org/t/p/w1280/xDGbZ0JJ3mYaGKy4Nzd9Kph6M9L.jpg	7.6	2024-11-20
519182	Despicable Me 4	Gru and Lucy and their girls—Margo, Edith and Agnes—welcome a new member to the Gru family, Gru Jr., who is intent on tormenting his dad. Gru also faces a new nemesis in Maxime Le Mal and his femme fatale girlfriend Valentina, forcing the family to go on the run.	https://image.tmdb.org/t/p/w1280/wWba3TaojhK7NdycRhoQpsG0FaH.jpg	7.1	2024-06-20
533535	Deadpool & Wolverine	A listless Wade Wilson toils away in civilian life with his days as the morally flexible mercenary, Deadpool, behind him. But when his homeworld faces an existential threat, Wade must reluctantly suit-up again with an even more reluctant Wolverine.	https://image.tmdb.org/t/p/w1280/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg	7.7	2024-07-24
539972	Kraven the Hunter	Kraven Kravinoff's complex relationship with his ruthless gangster father, Nikolai, starts him down a path of vengeance with brutal consequences, motivating him to become not only the greatest hunter in the world, but also one of its most feared.	https://image.tmdb.org/t/p/w1280/i47IUSsN126K11JUzqQIOi1Mg1M.jpg	5.5	2024-12-11
558449	Gladiator II	Years after witnessing the death of the revered hero Maximus at the hands of his uncle, Lucius is forced to enter the Colosseum after his home is conquered by the tyrannical Emperors who now lead Rome with an iron fist. With rage in his heart and the future of the Empire at stake, Lucius must look to his past to find strength and honor to return the glory of Rome to its people.	https://image.tmdb.org/t/p/w1280/2cxhvwyEwRlysAmRH4iodkvo0z5.jpg	6.688	2024-11-05
592983	Spellbound	When a powerful spell turns her parents into giant monsters, a teenage princess must journey into the wild to reverse the curse before it's too late.	https://image.tmdb.org/t/p/w1280/xFSIygDiX70Esp9dheCgGX0Nj77.jpg	6.913	2024-11-22
645757	That Christmas	It's an unforgettable Christmas for the townsfolk of Wellington-on-Sea when the worst snowstorm in history alters everyone's plans — including Santa's.	https://image.tmdb.org/t/p/w1280/bX6dx2U4hOk1esI7mYwtD3cEKdC.jpg	7.601	2024-11-27
698687	Transformers One	The untold origin story of Optimus Prime and Megatron, better known as sworn enemies, but once were friends bonded like brothers who changed the fate of Cybertron forever.	https://image.tmdb.org/t/p/w1280/qbkAqmmEIZfrCO8ZQAuIuVMlWoV.jpg	8.1	2024-09-11
762509	Mufasa: The Lion King	Rafiki relays the legend of Mufasa to lion cub Kiara, daughter of Simba and Nala, with Timon and Pumbaa lending their signature schtick. Told in flashbacks, the story introduces Mufasa as an orphaned cub, lost and alone until he meets a sympathetic lion named Taka—the heir to a royal bloodline. The chance meeting sets in motion a journey of misfits searching for their destiny and working together to evade a threatening and deadly foe.	https://image.tmdb.org/t/p/w1280/lurEK87kukWNaHd0zYnsi3yzJrs.jpg	8.2	2024-12-18
791042	Levels	After witnessing his girlfriend's murder, a man risks everything - including reality itself - to discover the truth.	https://image.tmdb.org/t/p/w1280/y1xm0jMIlx9Oo2a3jWNyLGm43sJ.jpg	5.808	2024-11-01
845781	Red One	After Santa Claus (codename: Red One) is kidnapped, the North Pole's Head of Security must team up with the world's most infamous tracker in a globe-trotting, action-packed mission to save Christmas.	https://image.tmdb.org/t/p/w1280/cdqLnri3NEGcmfnqwk2TSIYtddg.jpg	6.974	2024-10-31
912649	Venom: The Last Dance	Eddie and Venom are on the run. Hunted by both of their worlds and with the net closing in, the duo are forced into a devastating decision that will bring the curtains down on Venom and Eddie's last dance.	https://image.tmdb.org/t/p/w1280/aosm8NMQ3UyoBVpSxyimorCQykC.jpg	6.778	2024-10-22
933260	The Substance	A fading celebrity decides to use a black market drug, a cell-replicating substance that temporarily creates a younger, better version of herself.	https://image.tmdb.org/t/p/w1280/lqoMzCcZYEFK729d6qzt349fB4o.jpg	7.247	2024-09-07
939243	Sonic the Hedgehog 3	Sonic, Knuckles, and Tails reunite against a powerful new adversary, Shadow, a mysterious villain with powers unlike anything they have faced before. With their abilities outmatched in every way, Team Sonic must seek out an unlikely alliance in hopes of stopping Shadow and protecting the planet.	https://image.tmdb.org/t/p/w1280/d8Ryb8AunYAuycVKDp5HpdWPKgC.jpg	8	2024-12-19
945961	Alien: Romulus	While scavenging the deep ends of a derelict space station, a group of young space colonizers come face to face with the most terrifying life form in the universe.	https://image.tmdb.org/t/p/w1280/b33nnKl1GSFbao4l3fZDDqsMx0F.jpg	7.231	2024-08-13
957119	Sidelined: The QB and Me	Dallas, a burdened but headstrong dancer, is determined to get into the best dance school in the country—her late mother’s alma mater. However, that dream is suddenly derailed when the cheeky yet secretly grieving football star, Drayton, crashes into her life with a unique story of his own. Will the two of them be able to grow into their dreams together, or will their dreams be sidelined?	https://image.tmdb.org/t/p/w1280/hklQwv6QVoOp5bWyh1bjuF2ydyG.jpg	6.4	2024-11-29
972614	Knox Goes Away	A contract killer, after being diagnosed with a fast-moving form of dementia, is presented with the opportunity to redeem himself by saving the life of his estranged adult son. But to do so, he must race against the police closing in on him as well as the ticking clock of his own rapidly deteriorating mind.	https://image.tmdb.org/t/p/w1280/w39qKYjltCix18BwtoZ1e45usdb.jpg	6.9	2024-03-15
974453	Absolution	An aging ex-boxer gangster working as muscle for a Boston crime boss receives an upsetting diagnosis.  Despite a faltering memory, he attempts to rectify the sins of his past and reconnect with his estranged children. He is determined to leave a positive legacy for his grandson, but the criminal underworld isn’t done with him and won’t loosen their grip willingly.	https://image.tmdb.org/t/p/w1280/cNtAslrDhk1i3IOZ16vF7df6lMy.jpg	6.107	2024-10-31
995803	Arena Wars	In 2045 convicted criminals are given the opportunity to compete on the world's #1 televised sporting event, Arena Wars. They must survive 7 rooms and 7 of the most vicious killers in the country. If they win, they regain their freedom.	https://image.tmdb.org/t/p/w1280/4dRtXjk1rcsZlaMJpBn6Nh9cTfO.jpg	5.4	2024-06-25
1010581	My Fault	Noah must leave her city, boyfriend, and friends to move into William Leister's mansion, the flashy and wealthy husband of her mother Rafaela. As a proud and independent 17 year old, Noah resists living in a mansion surrounded by luxury. However, it is there where she meets Nick, her new stepbrother, and the clash of their strong personalities becomes evident from the very beginning.	https://image.tmdb.org/t/p/w1280/w46Vw536HwNnEzOa7J24YH9DPRS.jpg	7.917	2023-06-08
1022789	Inside Out 2	Teenager Riley's mind headquarters is undergoing a sudden demolition to make room for something entirely unexpected: new Emotions! Joy, Sadness, Anger, Fear and Disgust, who’ve long been running a successful operation by all accounts, aren’t sure how to feel when Anxiety shows up. And it looks like she’s not alone.	https://image.tmdb.org/t/p/w1280/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg	7.6	2024-06-11
1034541	Terrifier 3	Five years after surviving Art the Clown's Halloween massacre, Sienna and Jonathan are still struggling to rebuild their shattered lives. As the holiday season approaches, they try to embrace the Christmas spirit and leave the horrors of the past behind. But just when they think they're safe, Art returns, determined to turn their holiday cheer into a new nightmare. The festive season quickly unravels as Art unleashes his twisted brand of terror, proving that no holiday is safe.	https://image.tmdb.org/t/p/w1280/ju10W5gl3PPK3b7TjEmVOZap51I.jpg	6.842	2024-10-09
1035048	Elevation	A single father and two women venture from the safety of their homes to face monstrous creatures to save the life of a young boy.	https://image.tmdb.org/t/p/w1280/uQhYBxOVFU6s9agD49FnGHwJqG5.jpg	6.459	2024-11-07
1100782	Smile 2	About to embark on a new world tour, global pop sensation Skye Riley begins experiencing increasingly terrifying and inexplicable events. Overwhelmed by the escalating horrors and the pressures of fame, Skye is forced to face her dark past to regain control of her life before it spirals out of control.	https://image.tmdb.org/t/p/w1280/ht8Uv9QPv9y7K0RvUyJIaXOZTfd.jpg	6.6	2024-10-16
1118031	Apocalypse Z: The Beginning of the End	When a kind of rabies that transforms people into aggressive creatures spreads across the planet, Manel isolates himself at home with his cat, relying on his wits to survive; but soon they must go out in search of food, by land and by sea, dodging many dangers.	https://image.tmdb.org/t/p/w1280/wIGJnIFQlESkC2rLpfA8EDHqk4g.jpg	6.9	2024-10-04
1138194	Heretic	Two young missionaries are forced to prove their faith when they knock on the wrong door and are greeted by a diabolical Mr. Reed, becoming ensnared in his deadly game of cat-and-mouse.	https://image.tmdb.org/t/p/w1280/5HJqjCTcaE1TFwnNh3Dn21be2es.jpg	7.092	2024-10-31
1147416	Miraculous World, London: At the Edge of Time	To save the future from a terrible fate, Marinette becomes Chronobug and teams up with Bunnyx to defeat a mysterious opponent who travels through time. Who is this new supervillain, and why are they obsessed with exposing Marinette's secret superhero identity? Marinette's only hope is to defeat her new opponent to prevent the end of Ladybug and time itself!	https://image.tmdb.org/t/p/w1280/6AtoMpHvs9pxd30KsyK8QmJ9W9M.jpg	8.5	2024-11-14
1154223	Hunting With Tigers	Malik, a young Parisian hustler, discovers that his stepfather Serge, a famous bank robber, has been arrested along with his accomplices. During the trial, Iris, one of the accused's lawyers, Chérif, requests Malik to accept a dangerous heist in exchange for Serge and her client's liberty. Malik must convince and reunite Chérif's former partners to accomplish this high-risk stickup.	https://image.tmdb.org/t/p/w1280/vb6qzT0egUPHcmUwusPNl9j943p.jpg	6.2	2024-11-22
1155095	The Moor	Claire is approached by the father of her murdered childhood friend to help investigate the haunted moor he believes is his son's final resting place.	https://image.tmdb.org/t/p/w1280/xZ9kdSBEoJNkzZPvQOVzS1uLMk6.jpg	4.5	2024-06-14
1167271	Weekend in Taipei	A former DEA agent and a former undercover operative revisit their romance during a fateful weekend in Taipei, unaware of the dangerous consequences of their past.	https://image.tmdb.org/t/p/w1280/qSc0AUvs8mRy00R9y8QYEHWIAQ9.jpg	6.181	2024-09-19
1171640	GTMAX	When a notorious gang of bikers recruits her brother for a heist, a former motocross champion must face her deepest fears to keep her family safe.	https://image.tmdb.org/t/p/w1280/bx92hl70NUhojjO3eV6LqKllj4L.jpg	6.149	2024-11-19
1182387	Armor	Armored truck security guard James Brody is working with his son Casey transporting millions of dollars between banks when a team of thieves led by Rook orchestrate a takeover of their truck to seize the riches. Following a violent car chase, Rook soon has the armored truck surrounded and James and Casey find themselves cornered onto a decrepit bridge.	https://image.tmdb.org/t/p/w1280/pnXLFioDeftqjlCVlRmXvIdMsdP.jpg	5.5	2024-10-30
1184918	The Wild Robot	After a shipwreck, an intelligent robot called Roz is stranded on an uninhabited island. To survive the harsh environment, Roz bonds with the island's animals and cares for an orphaned baby goose.	https://image.tmdb.org/t/p/w1280/wTnV3PCVW5O92JMrFvvrRcV39RU.jpg	8.4	2024-09-08
1241982	Moana 2	After receiving an unexpected call from her wayfinding ancestors, Moana journeys alongside Maui and a new crew to the far seas of Oceania and into dangerous, long-lost waters for an adventure unlike anything she's ever faced.	https://image.tmdb.org/t/p/w1280/4YZpsylmjHbqeWzjKpUEF8gcLNW.jpg	6.911	2024-11-21
1252470	Sikandar Ka Muqaddar	After an unsolved diamond heist, a hard-nosed cop’s pursuit of his key suspect turns into obsession, until they finally face each other — and the truth.	https://image.tmdb.org/t/p/w1280/eWUh4rgxtgypgnOa6uGMnUt01ux.jpg	6	2024-11-29
1299652	Watchmen: Chapter II	Suspicious of the events ensnaring their former colleagues, Nite Owl and Silk Spectre are spurred out of retirement to investigate. As they grapple with personal ethics, inner demons and a society turned against them, they race the clock to uncover a deepening plot that might trigger global nuclear war.	https://image.tmdb.org/t/p/w1280/4rBObJFpiWJOG7aIlRrOUniAkBs.jpg	7.542	2024-11-25
1326059	Pimpinero: Blood and Oil	When Juan, a young gasoline smuggler, is forced to work for a mysterious organization in the desert bordering Colombia and Venezuela, his girlfriend Diana embarks on a journey to uncover the secrets that inhabit this no-man’s-land.	https://image.tmdb.org/t/p/w1280/kukotsflOSVGXQezuXohj41dbfL.jpg	7.2	2024-10-10
1357633	Solo Leveling -ReAwakening-	Over a decade after 'gates' connecting worlds appeared, awakening 'hunters' with superpowers, weakest hunter Sung Jinwoo encounters a double dungeon and accepts a mysterious quest, becoming the only one able to level up, changing his fate. A catch-up recap of the first season coupled with an exclusive sneak peek of the first two episodes of the highly anticipated second season in one momentous theatrical fan experience.	https://image.tmdb.org/t/p/w1280/uzHMp5heVLR68kbbUEXFPsmxYsM.jpg	8.091	2024-11-26
\.


--
-- Data for Name: all_reviews; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.all_reviews (movie_id, username, rating, review) FROM stdin;
519182	Moultrie	1	Gru didnt steal the mood
\.


--
-- Name: all_movies all_movies_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.all_movies
    ADD CONSTRAINT all_movies_pkey PRIMARY KEY (movie_id);


--
-- Name: all_reviews all_reviews_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.all_reviews
    ADD CONSTRAINT all_reviews_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.all_movies(movie_id);


--
-- PostgreSQL database dump complete
--

