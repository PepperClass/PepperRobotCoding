<?xml version="1.0" encoding="UTF-8" ?>
<Package name="GoogleNaturalLanguageAPIPepper" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
    </Dialogs>
    <Resources>
        <File name="index" src="html/index.html" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
        <Topic name="ExampleDialog_mnc" src="behavior_1/ExampleDialog/ExampleDialog_mnc.top" topicName="ExampleDialog" language="zh_CN" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_zh_CN" src="translations/translation_zh_CN.ts" language="zh_CN" />
    </Translations>
</Package>
