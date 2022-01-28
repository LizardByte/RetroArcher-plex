import os
import plistlib

version = os.getenv('BUILD_VERSION', "development build")

if version == "development build":
    checked = '<i class="fas fa-fw fa-times-circle" style="color:red"></i>'
else:
    checked = '<i class="fas fa-fw fa-check-circle" style="color:green"></i>'

info_file = os.path.join('Contents', 'Info.plist')

pl = dict(
    CFBundleIdentifier="com.github.agents.retroarcher.retroarcher",
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
                <strong>RetroArcher.bundle</strong><br>
            </div>
            <br>
            <a href="https://www.nullreferer.com/?https://retroarcher.github.io" target="_blank">RetroArcher</a> is a
            gaming plug-in for Plex Media Server! The goal of RetroArcher is to use Plex as a gaming front end interface
            and then use proven game streaming technology to stream your gameplay to any of your standard Plex clients.
            Simply put RetroArcher is to video games, what Plex is to multimedia.<br>
            <br>
            <table>
                <tr>
                    <td>Version:  %s</td>
                    <td>%s</td><!-- Brackets with version number indicate pre RetroArcher.X integration -->
                    <td>| <a href="https://github.com/RetroArcher/RetroArcher.bundle/releases/latest" target="_blank">Releases</a></td>
                </tr>
            </table>
            <br>
            <table>
                <tr>
                    <td><i class="fa fa-fw fa-question-circle"></i> Reference:</td>
                    <td>| <i class="fa fa-fw fa-list-alt"></i> <a href="https://github.com/RetroArcher/RetroArcher.bundle/wiki" target="_blank">Docs</a></td>
                </tr>
                <tr>
                    <td><i class="fa fa-fw fa-comment"></i> Social:</td>
                    <td>| <i class="fab fa-fw fa-facebook"></i> <a href="https://www.facebook.com/RetroArcherFB" target="_blank">Facebook</a></td>
                    <td>| <i class="fab fa-fw fa-twitter"></i> <a href="https://twitter.com/RetroArcherTW" target="_blank">Twitter</a></td>
                    <td>| <i class="fab fa-fw fa-youtube"></i> <a href="https://www.youtube.com/channel/UCtSzs1U8B7yYX1uE58a6BxA" target="_blank">YouTube</a></td>
                </tr>
                <tr>
                    <td><i class="fa fa-fw fa-exclamation-triangle"></i> Support:</td>
                    <td>| <i class="fab fa-fw fa-discord"></i> <a href="https://retroarcher.github.io/discord_join" target="_blank">Discord</a></td>
                    <td>| <i class="fab fa-fw fa-facebook-f"></i> <a href="https://www.facebook.com/groups/retroracher" target="_blank">Facebook Group</a></td>
                    <td>| <i class="fab fa-fw fa-reddit-alien"></i> <a href="https://reddit.com/r/RetroArcher" target="_blank">Reddit</a></td>
                </tr>
                <tr>
                    <td><i class="fa fa-fw fa-donate"></i> Donate:</td>
                    <td>| <i class="fab fa-fw fa-github-alt"></i> <a href="https://github.com/sponsors/ReenigneArcher" target="_blank">Github</a></td>
                    <td>| <i class="fab fa-fw fa-patreon"></i> <a href="https://patreon.com/RetroArcher" target="_blank">Patreon</a></td>
                    <td>| <i class="fab fa-fw fa-paypal"></i> <a href="https://paypal.me/ReenigneArcher" target="_blank">Paypal</a></td>
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
    PlexPluginClass="agent",
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

with open(info_file, 'wb') as fp:
    plistlib.dump(value=pl, fp=fp)
