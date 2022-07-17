import instaloader

bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, input('Введите username пользователя: '))

print("Username :", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
# print("Bio: ", profile.boigraphy)  If available
print("Link in Boi: ", profile.external_url)


# ATTENTION!
# This parser only returns profile information.