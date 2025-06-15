import re


from .. import rule as rule_model
from .. import entities
from ....platform.types import message as platform_message
import langbot_plugin.api.entities.builtin.pipeline.query as pipeline_query


@rule_model.rule_class('regexp')
class RegExpRule(rule_model.GroupRespondRule):
    async def match(
        self,
        message_text: str,
        message_chain: platform_message.MessageChain,
        rule_dict: dict,
        query: pipeline_query.Query,
    ) -> entities.RuleJudgeResult:
        regexps = rule_dict['regexp']

        for regexp in regexps:
            match = re.match(regexp, message_text)

            if match:
                return entities.RuleJudgeResult(
                    matching=True,
                    replacement=message_chain,
                )

        return entities.RuleJudgeResult(matching=False, replacement=message_chain)
