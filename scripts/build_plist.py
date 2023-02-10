import os
import plistlib

version = os.getenv('BUILD_VERSION', None)
print('version: %s' % version)

commit = os.getenv('GITHUB_SHA', 'development build')
print('commit: %s' % commit)

if not version:
    checked = '<i class="fas fa-fw fa-times-circle" style="color:red"></i>'
    if commit != 'development build':
        version = commit[0:7]
        print('using commit as version: %s' % version)
    else:
        version = commit
        print('unknown version: %s' % version)
else:
    checked = '<i class="fas fa-fw fa-check-circle" style="color:green"></i>'

info_file = os.path.join('Contents', 'Info.plist')

pl = dict(
    CFBundleIdentifier="dev.lizardbyte.retroarcher-plex",
    PlexAgentAttributionText="""
        <![CDATA[
            <!-- Import custom css -->
            <style>
                @import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css");
            </style>
            <style>
                div.center {
                    text-align: center;
                }
            </style>

            <div class="center">
                <strong>RetroArcher-plex</strong><br>
            </div>
            <br>
            <a href="https://app.lizardbyte.dev" target="_blank">RetroArcher</a> is a
            gaming plug-in for Plex Media Server! The goal of RetroArcher is to use Plex as a gaming front end interface
            and then use proven game streaming technology to stream your gameplay to any of your standard Plex clients.
            Simply put RetroArcher is to video games, what Plex is to multimedia.<br>
            <br>
            <table>
                <tr>
                    <td>Version:  %s</td>
                    <td>%s</td>
                    <td>| <a href="https://github.com/LizardByte/RetroArcher-plex/releases/latest"
                             target="_blank">Releases</a></td>
                </tr>
            </table>
            <br>
            <table>
                <tr>
                    <td><i class="fa fa-fw fa-question-circle"></i> Reference:</td>
                    <td>| <i class="fa-solid fa-fw fa-file-lines"></i> <a
                            href="https://retroarcher-plex.readthedocs.io/en/latest/" target="_blank">Docs</a></td>
                </tr>
                <tr>
                    <td><i class="fa fa-fw fa-comment"></i> Social:</td>
                    <td>| <i class="fab fa-fw fa-facebook"></i> <a href="https://www.facebook.com/LizardByteDev"
                                                                   target="_blank">Facebook</a></td>
                    <td>| <i class="fab fa-fw fa-twitter"></i> <a href="https://twitter.com/LizardByteDev"
                                                                  target="_blank">Twitter</a></td>
                    <td>| <i class="fab fa-fw fa-youtube"></i> <a href="https://www.youtube.com/c/LizardByteDev"
                                                                  target="_blank">YouTube</a></td>
                </tr>
                <tr>
                    <td><i class="fa fa-fw fa-exclamation-triangle"></i> Support:</td>
                    <td>| <i class="fab fa-fw fa-discord"></i> <a href="https://app.lizardbyte.dev/discord"
                                                                  target="_blank">Discord</a></td>
                    <td>| <i class="fab fa-fw fa-facebook-f"></i> <a href="https://www.facebook.com/groups/lizardbyte"
                                                                     target="_blank">Facebook Group</a></td>
                    <td>| <i class="fab fa-fw fa-reddit-alien"></i> <a href="https://reddit.com/r/LizardByte"
                                                                       target="_blank">Reddit</a></td>
                </tr>
                <tr>
                    <td><i class="fa fa-fw fa-donate"></i> Donate:</td>
                    <td>| <i class="fab fa-fw fa-github"></i> <a href="https://github.com/sponsors/LizardByte"
                                                                 target="_blank">Github</a></td>
                    <td>| <i class="fab fa-fw fa-patreon"></i> <a href="https://patreon.com/LizardByte"
                                                                  target="_blank">Patreon</a></td>
                    <td>| <i class="fab fa-fw fa-paypal"></i> <a href="https://paypal.me/ReenigneArcher"
                                                                 target="_blank">Paypal</a></td>
                </tr>
            </table>
            <div class="center">
                <i class="fa fa-fw fa-gamepad" style="font-size:80px;"></i>
            </div>

            <script>
                <!-- Javascript here -->
                <!-- Can probably show link only when a newer release is found. -->
            </script>
        ]]>
    """ % (checked, version),
    PlexFrameworkVersion="2",
    PlexPluginClass="Agent",
    PlexPluginMode="Agent",
    PlexClientPlatforms="",
    PlexClientPlatformExclusions="",
    PlexPluginRegions=[""],
    PlexPluginDebug=["1"],
    PlexPluginCodePolicy="Elevated",
    PlexPluginConsoleLogging="0",
)

# PlexPluginMode:
# This one does nothing with a value of "Always On", a value of "daemon" keeps the plugin alive in the background.

# PlexClientPlatforms and PlexClientPlatformExclusions:
# Any Clients support or not supported by the plugin.
# Possible values are * for all platforms, MacOSX, Windows, Linux, Roku, Android, iOS, Safari, Firefox, Chrome, LGTV, \
# Samsung, PlexConnect and Plex Home Theater

# PlexPluginRegions:
# Possible string values are the proper ISO two letter code for the country.
# A full list of values are available at http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

# PlexPluginDebug:
# Possible values are 0 and 1. Setting it to "1" rather than "0" turns on debug logging

# PlexPluginCodePolicy:
# This allows channels to access some python methods which are otherwise blocked, as well as import external code \
# libraries, and interact with the PMS HTTP API

# PlexPluginClass:
# This key is used to show that the plugin is an agent. possible values are agent

# PlexPluginConsoleLogging:
# This is used to send plugin log statements directly to stout when running PMS from the command line. \
# Rarely used anymore

plist_string = plistlib.writePlistToString(pl).replace('&lt;', '<').replace('&gt;', '>')

with open(info_file, 'wb') as fp:
    fp.write(plist_string)
