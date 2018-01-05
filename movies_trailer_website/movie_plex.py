import fresh_tomatoes
import media

dangal = media.Movie("DANGAL",
                     "Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle glory at the Commonwealth Games in the face of societal oppression.",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")


#print(dangal.storyline)

jagga_jasoos = media.Movie("Jagga Jasoos",
                           "Join Jagga, a gifted teenage detective, who along with a female companion, is on a quest to find his missing father.",
                           "https://upload.wikimedia.org/wikipedia/en/9/94/JaggaJasoosPoster.jpg",
                           "https://www.youtube.com/watch?v=xtm48kJwL1I")

#dangal.show_trailer()

bahubali_2 = media.Movie("Bahubali 2:The Conclusion",
                         "When Shiva, the son of Bahubali, learns about his heritage, he begins to look for answers. His story is juxtaposed with past events that unfolded in the Mahishmati Kingdom.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                         "https://www.youtube.com/watch?v=G62HrubdD6o")

a_gentleman = media.Movie("A Gentleman",
                           "Gaurav is on a mission to settle down. He is in the process of trying to charm Kavya into creating life with him and getting married. However, Kavya dreads the thought of taking the plunge and settling down. Her only wish is that her sundar sushil gentleman lives life to the full, with a little more risk and excitement. However, things take an interesting twist when an assignment takes Gaurav to Mumbai.",
                           "https://upload.wikimedia.org/wikipedia/en/c/c6/A_Gentleman.jpg",
                           "https://www.youtube.com/watch?v=IMXifj-peiQ")

baadshaho = media.Movie("Baadshaho",
                         "Baadshaho is inspired by real-life events during the Emergency and revolves around stolen gold, a thief (Ajay Devgn), an undercover cop (Vidyut Jammwal), a character inspired by Maharani Gayatri Devi (Ileana D'Cruz) and an army officer (Emraan Hashmi) who is entrusted with protecting the country's treasure.",
                         "https://upload.wikimedia.org/wikipedia/en/c/ce/Ajay_Devgn%27s_Baadshaho.JPG",
                         "https://www.youtube.com/watch?v=Ny7fULat8ws")

simran = media.Movie("SIMRAN",
                      "A Gujarati housekeeping lady in the US allows ambition to get the better of her & gets involved in a world of crime. Simran is a racy, fun film with Kangana Ranaut playing the titular role.",
                      "https://upload.wikimedia.org/wikipedia/en/d/d3/Simran_Poster.jpg",
                      "https://www.youtube.com/watch?v=_LUe4r6eeQA")

movies = [dangal, jagga_jasoos, bahubali_2, a_gentleman, baadshaho, simran]
fresh_tomatoes.open_movies_page(movies)
